
# # Updated Advanced code

# import sqlite3
# import json
# from datetime import datetime

# DB_FILE = "titan_corp.db"

# def initialize_titan_db():
#     """Initializes the multi-table architecture including markets, ledgers, and audit trails."""
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()

#         # 1. Financial Ledger
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS corporate_ledgers (
#                 executive TEXT PRIMARY KEY,
#                 cash_balance REAL,
#                 stock_holdings TEXT,
#                 portfolio_value_history TEXT
#             )
#         ''')

#         # 2. Logistics Inventory
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS supply_chain_inventory (
#                 executive TEXT PRIMARY KEY,
#                 raw_material_units INTEGER,
#                 finished_goods_units INTEGER,
#                 active_freight_containers TEXT
#             )
#         ''')

#         # 3. System Logs
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS system_logs (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 executive TEXT,
#                 timestamp DATETIME,
#                 log_type TEXT,
#                 message TEXT
#             )
#         ''')

#         # 4. Cryptographic Secure Vault
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS security_audit_vault (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 timestamp DATETIME,
#                 executive TEXT,
#                 action_type TEXT,
#                 details TEXT,
#                 secure_hash TEXT
#             )
#         ''')

#         # 🌐 NEW 200% LEVEL TABLE: Dynamic Macro Market Environment Metrics
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS global_market_state (
#                 key TEXT PRIMARY KEY,
#                 value_data TEXT
#             )
#         ''')
#         conn.commit()

# def seed_initial_corporate_state():
#     """Seeds the baseline variables for executives and initializes dynamic market prices."""
#     executives = ["Warren", "George", "Ray", "Cathie"]
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         for name in executives:
#             cursor.execute('''
#                 INSERT OR IGNORE INTO corporate_ledgers (executive, cash_balance, stock_holdings, portfolio_value_history)
#                 VALUES (?, 10000.0, '{}', '[]')
#             ''', (name,))

#             cursor.execute('''
#                 INSERT OR IGNORE INTO supply_chain_inventory (executive, raw_material_units, finished_goods_units, active_freight_containers)
#                 VALUES (?, 50, 10, '[]')
#             ''', (name,))
        
#         # Seed initial dynamic stock market prices and global environment constants
#         initial_prices = {"AAPL": 150.0, "TSLA": 200.0, "NVDA": 100.0, "AMZN": 120.0, "RAW_COST": 50.0, "RETAIL_VALUE": 400.0}
#         cursor.execute('''
#             INSERT OR IGNORE INTO global_market_state (key, value_data)
#             VALUES ('prices', ?)
#         ''', (json.dumps(initial_prices),))
        
#         cursor.execute('''
#             INSERT OR IGNORE INTO global_market_state (key, value_data)
#             VALUES ('macro_news', 'Global markets trading within normal parameters. Supply chain paths stable.')
#         ''')
#         conn.commit()

# def write_system_log(executive: str, log_type: str, message: str):
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO system_logs (executive, timestamp, log_type, message)
#             VALUES (?, datetime('now'), ?, ?)
#         ''', (executive.capitalize(), log_type, message))
#         conn.commit()

# if __name__ == "__main__":
#     initialize_titan_db()
#     seed_initial_corporate_state()
#     print("✨ 200% Advanced Titan Database Infrastructure Rebuilt Successfully!")


# central Advaned code

import sqlite3
import json
from datetime import datetime

DB_FILE = "titan_corp.db"

def initialize_titan_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Clean Financial Ledger
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS corporate_ledgers (
                executive TEXT PRIMARY KEY,
                cash_balance REAL,
                stock_holdings TEXT,
                portfolio_value_history TEXT
            )
        ''')
        # Clean Logistics Supply Stack
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS supply_chain_inventory (
                executive TEXT PRIMARY KEY,
                raw_material_units INTEGER,
                finished_goods_units INTEGER
            )
        ''')
        # UI Log System Feed
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                executive TEXT,
                timestamp DATETIME,
                log_type TEXT,
                message TEXT
            )
        ''')
        # Audit Trail Tracker
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS security_audit_vault (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                executive TEXT,
                action_type TEXT,
                details TEXT
            )
        ''')
        # Live Shared Market State Tickers
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS global_market_state (
                key TEXT PRIMARY KEY,
                value_data TEXT
            )
        ''')
        conn.commit()

def seed_initial_corporate_state():
    executives = ["Warren", "George", "Ray", "Cathie"]
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        for name in executives:
            cursor.execute('INSERT OR IGNORE INTO corporate_ledgers VALUES (?, 10000.0, "{}", "[]")', (name,))
            cursor.execute('INSERT OR IGNORE INTO supply_chain_inventory VALUES (?, 50, 10)', (name,))
        
        initial_prices = {"AAPL": 150.0, "TSLA": 200.0, "NVDA": 100.0, "AMZN": 120.0, "RAW_COST": 50.0, "RETAIL_VALUE": 400.0}
        cursor.execute("INSERT OR IGNORE INTO global_market_state VALUES ('prices', ?)", (json.dumps(initial_prices),))
        conn.commit()

def write_system_log(executive: str, log_type: str, message: str):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO system_logs (executive, timestamp, log_type, message) VALUES (?, datetime('now'), ?, ?)", (executive.capitalize(), log_type, message))
        conn.commit()

if __name__ == "__main__":
    initialize_titan_db()
    seed_initial_corporate_state()
    print("✨ Clean & Simplified Database Infrastructure Formed!")