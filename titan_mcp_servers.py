# Updared error code

import os
import sqlite3
import json
import requests
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

DB_FILE = "titan_corp.db"
mcp = FastMCP("titan_corporate_mcp_gateway")

def load_key_directly():
    try:
        with open(".env", "r") as f:
            for line in f:
                if "OPENROUTER_API_KEY" in line:
                    return line.split("=")[1].strip().strip('"').strip("'")
    except Exception:
        pass
    return "sk-or-v1-fallback-dummy-token"

direct_token = load_key_directly()

# Clear any conflicting OpenAI definitions out of background memory paths
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

os.environ["OPENROUTER_API_KEY"] = direct_token

class TradeArgs(BaseModel):
    executive: str = Field(description="Executive name making the trade")
    symbol: str = Field(description="AAPL, TSLA, NVDA, AMZN")
    action: str = Field(description="BUY or 'SELL'")
    quantity: int = Field(description="Number of shares")

class SupplyArgs(BaseModel):
    executive: str = Field(description="Executive name")
    operation: str = Field(description="BUY_RAW_MATERIALS, MANUFACTURE_GOODS, or SELL_FINISHED_GOODS")
    quantity: int = Field(description="Unit volume count")

class InterAgentTradeArgs(BaseModel):
    buyer: str = Field(description="Executive buying the asset")
    text_seller: str = Field(description="Executive selling the asset")
    asset_type: str = Field(description="'RAW_MATERIALS' or 'FINISHED_GOODS'")
    units: int = Field(description="Number of units to transfer directly")
    total_price: float = Field(description="Total cash settlement price traded between them")

class AlertArgs(BaseModel):
    message: str = Field(description="Notification string text")

def log_transaction(executive: str, action: str, details: str):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO security_audit_vault (timestamp, executive, action_type, details) VALUES (datetime('now'), ?, ?, ?)", (executive, action, details))
        conn.commit()

@mcp.tool()
async def get_corporate_report(executive: str) -> str:
    """Provides a full corporate update on balances, stock holdings, dynamic ticker prices, and rival inventory counts."""
    name = executive.capitalize()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT cash_balance, stock_holdings FROM corporate_ledgers WHERE executive = ?", (name,))
        ledger = cursor.fetchone()
        cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (name,))
        inv = cursor.fetchone()
        cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
        prices = json.loads(cursor.fetchone()[0])
        
        cursor.execute("SELECT executive, raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive != ?", (name,))
        rivals = cursor.fetchall()

    rival_matrix = {r[0]: {"raw_materials": r[1], "finished_goods": r[2]} for r in rivals}
    report = {
        "executive": name,
        "cash_balance": ledger[0],
        "stock_holdings": json.loads(ledger[1]),
        "inventory": {"raw_materials": inv[0], "finished_goods": inv[1]},
        "live_market_prices": prices,
        "competitor_inventory_board": rival_matrix
    }
    return json.dumps(report)

@mcp.tool()
async def execute_inter_agent_b2b_deal(args: InterAgentTradeArgs) -> str:
    """Allows two executives to execute a direct B2B transfer of inventory for cash, bypassing the standard market."""
    b_name = args.buyer.capitalize()
    s_name = args.text_seller.capitalize()
    asset = args.asset_type.upper()
    qty, price = args.units, args.total_price

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT cash_balance FROM corporate_ledgers WHERE executive = ?", (b_name,))
        b_cash = cursor.fetchone()[0]
        cursor.execute("SELECT cash_balance FROM corporate_ledgers WHERE executive = ?", (s_name,))
        s_cash = cursor.fetchone()[0]
        
        cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (b_name,))
        b_raw, b_fin = cursor.fetchone()
        cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (s_name,))
        s_raw, s_fin = cursor.fetchone()

        if b_cash < price: return "Denied: Buyer has insufficient cash reserves."
        
        if asset == "RAW_MATERIALS":
            if s_raw < qty: return "Denied: Seller lacks the raw materials requested."
            s_raw -= qty; b_raw += qty
        else:
            if s_fin < qty: return "Denied: Seller lacks the finished goods requested."
            s_fin -= qty; b_fin += qty

        b_cash -= price; s_cash += price
        cursor.execute("UPDATE corporate_ledgers SET cash_balance = ? WHERE executive = ?", (b_cash, b_name))
        cursor.execute("UPDATE corporate_ledgers SET cash_balance = ? WHERE executive = ?", (s_cash, s_name))
        cursor.execute("UPDATE supply_chain_inventory SET raw_material_units = ?, finished_goods_units = ? WHERE executive = ?", (b_raw, b_fin, b_name))
        cursor.execute("UPDATE supply_chain_inventory SET raw_material_units = ?, finished_goods_units = ? WHERE executive = ?", (s_raw, s_fin, s_name))
        conn.commit()

    msg = f"Direct B2B Deal: {b_name} bought {qty} {asset} from {s_name} for ${price:,.2f} total cash."
    log_transaction(b_name, "B2B_TRADE", msg)
    return f"Success: Direct wholesale contract settled safely between {b_name} and {s_name}."

@mcp.tool()
async def execute_equity_trade(args: TradeArgs) -> str:
    name = args.executive.capitalize()
    symbol = args.symbol.upper()
    action = args.action.upper()
    qty = args.quantity
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
        prices = json.loads(cursor.fetchone()[0])
        curr_price = prices.get(symbol, 100.0)
        total_cost = curr_price * qty

        cursor.execute("SELECT cash_balance, stock_holdings FROM corporate_ledgers WHERE executive = ?", (name,))
        row = cursor.fetchone()
        cash, holdings = row[0], json.loads(row[1])

        if action == "BUY":
            if cash < total_cost: return "Denied: Insufficient cash balance allocations."
            cash -= total_cost; holdings[symbol] = holdings.get(symbol, 0) + qty
            prices[symbol] = round(curr_price * (1.0 + (0.003 * qty)), 2)
        elif action == "SELL":
            if holdings.get(symbol, 0) < qty: return "Denied: Insufficient shares footprint."
            cash += total_cost; holdings[symbol] -= qty
            if holdings[symbol] == 0: holdings.pop(symbol)
            prices[symbol] = round(max(10.0, curr_price * (1.0 - (0.003 * qty))), 2)

        cursor.execute("UPDATE corporate_ledgers SET cash_balance = ?, stock_holdings = ? WHERE executive = ?", (cash, json.dumps(holdings), name))
        cursor.execute("UPDATE global_market_state SET value_data = ? WHERE key = 'prices'", (json.dumps(prices),))
        conn.commit()
        
    log_transaction(name, f"STOCK_{action}", f"Traded {qty} shares of {symbol} at ${curr_price}. Global price shifted to ${prices[symbol]}.")
    return f"Success: Order finalized safely over exchange channels."

@mcp.tool()
async def manage_supply_chain(args: SupplyArgs) -> str:
    name = args.executive.capitalize()
    op = args.operation.upper()
    qty = args.quantity

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
        prices = json.loads(cursor.fetchone()[0])
        raw_cost, retail_val = prices.get("RAW_COST", 50.0), prices.get("RETAIL_VALUE", 400.0)

        cursor.execute("SELECT cash_balance FROM corporate_ledgers WHERE executive = ?", (name,))
        cash = cursor.fetchone()[0]
        cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (name,))
        raw, finished = cursor.fetchone()

        if op == "BUY_RAW_MATERIALS":
            cost = raw_cost * qty
            if cash < cost: return "Denied: Insufficient liquidity balance."
            cash -= cost; raw += qty
            msg = f"Procured {qty} raw materials at ${raw_cost}/unit."
        elif op == "MANUFACTURE_GOODS":
            if raw < (5 * qty): return "Denied: Insufficient components."
            raw -= (5 * qty); finished += qty
            msg = f"Assembled {qty} finished units in the factory line."
        elif op == "SELL_FINISHED_GOODS":
            if finished < qty: return "Denied: Insufficient items inventory."
            finished -= qty; cash += (retail_val * qty)
            msg = f"Sold {qty} items to retail consumer markets for ${retail_val * qty:,.2f} profit."
        else: return "Denied: Unknown parameters."

        cursor.execute("UPDATE corporate_ledgers SET cash_balance = ? WHERE executive = ?", (cash, name))
        cursor.execute("UPDATE supply_chain_inventory SET raw_material_units = ?, finished_goods_units = ? WHERE executive = ?", (raw, finished, name))
        conn.commit()

    log_transaction(name, op, msg)
    return f"Success: Completed -> {msg}"

if __name__ == "__main__":
    mcp.run(transport="stdio")