# # next level code Advanced
# import gradio as gr
# import sqlite3
# import json
# import pandas as pd
# import plotly.graph_objects as go
# from datetime import datetime
# from openai import AsyncOpenAI
# import os
# import asyncio
# from dotenv import load_dotenv

# DB_FILE = "titan_corp.db"

# # Initialize environment variables safely
# load_dotenv()

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# openrouter_client = AsyncOpenAI(
#     base_url="https://openrouter.ai/api/v1", 
#     api_key=OPENROUTER_API_KEY
# )

# # PREMIUM LIGHT PLATINUM EXECUTIVE WORKSPACE CSS STYLESHEET
# premium_light_css = """
# .gradio-container { background-color: #f4f6f9 !important; color: #2d3748 !important; font-family: 'Segoe UI', sans-serif !important; }
# #master-header { text-align: center; border-bottom: 3px solid #1a365d; padding-bottom: 12px; margin-bottom: 20px; background: #ffffff; padding-top: 12px; border-radius: 6px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
# #master-header h1 { color: #1a365d; margin: 0; font-weight: 700; font-size: 2.1rem; text-transform: uppercase; letter-spacing: 1px; }
# .block { border: 1px solid #e2e8f0 !important; background: #ffffff !important; border-radius: 8px !important; box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important; }
# .tabs { background: #ffffff !important; border: 1px solid #e2e8f0 !important; border-radius: 8px !important; }
# .tab-nav { border-bottom: 2px solid #e2e8f0 !important; background: #f8fafc !important; }
# .tab-nav button { font-weight: 600 !important; color: #4a5568 !important; }
# .tab-nav button.selected { border-bottom: 3px solid #3182ce !important; color: #2b6cb0 !important; background: #ffffff !important; }
# .scroll-feed-container { background-color: #f8fafc !important; border: 1px solid #cbd5e0 !important; border-radius: 6px !important; padding: 15px !important; height: 320px !important; overflow-y: scroll !important; }
# .scroll-feed-container div { border-bottom: 1px dashed #e2e8f0; padding-bottom: 6px; margin-bottom: 8px; font-size: 13.5px; }
# .stat-box { background: #ebf8ff !important; border-left: 4px solid #3182ce !important; }
# .control-btn { font-weight: bold !important; border-radius: 6px !important; }
# footer { visibility: hidden !important; }
# """

# force_light_js = "function() { const url = new URL(window.location); if (url.searchParams.get('__theme') !== 'light') { url.searchParams.set('__theme', 'light'); window.location.href = url.href; } }"

# def fetch_global_leaderboard_chart():
#     executives = ["Warren", "George", "Ray", "Cathie"]
#     colors = {"Warren": "#2b6cb0", "George": "#4a5568", "Ray": "#2f855a", "Cathie": "#dd6b20"}
#     fig = go.Figure()
#     try:
#         with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#             cursor = conn.cursor()
#             for name in executives:
#                 cursor.execute("SELECT portfolio_value_history FROM corporate_ledgers WHERE executive = ?", (name,))
#                 row = cursor.fetchone()
#                 if row and row[0]:
#                     history = json.loads(row[0])
#                     if history:
#                         df = pd.DataFrame(history)
#                         if not df.empty and "time" in df.columns:
#                             fig.add_trace(go.Scatter(
#                                 x=df["time"], y=df["worth"], mode="lines+markers",
#                                 name=f"CFO {name}", line=dict(color=colors[name], width=3), marker=dict(size=5)
#                             ))
#     except Exception:
#         pass
#     fig.update_layout(
#         title="📊 Global Corporate Leaderboard Network (Real-Time Net Worth Race)",
#         paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc", font_color="#2d3748", title_font_color="#1a365d",
#         margin=dict(l=40, r=30, t=40, b=40), xaxis=dict(gridcolor="#e2e8f0", title="System Timeline Clock"),
#         yaxis=dict(gridcolor="#e2e8f0", title="Unified Net Capitalization (USD)")
#     )
#     return fig

# def fetch_global_market_status():
#     try:
#         with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])
#             cursor.execute("SELECT timestamp, executive, action_type, details FROM security_audit_vault ORDER BY id DESC LIMIT 6")
#             vault_rows = cursor.fetchall()
#     except Exception:
#         return pd.DataFrame(), pd.DataFrame(), fetch_global_leaderboard_chart()

#     ticker_df = pd.DataFrame([{"Asset Ticker": k, "Exchange Price / Cost": f"${v:,.2f}"} for k, v in prices.items()])
#     vault_df = pd.DataFrame([{"Timestamp": r[0], "Executive Officer": r[1], "Verified Corporate Action": r[3], "Status": "✅ VERIFIED"} for r in vault_rows] if vault_rows else [{"Timestamp": "-", "Executive Officer": "-", "Verified Corporate Action": "Awaiting operations loop steps...", "Status": "-"}])
#     return ticker_df, vault_df, fetch_global_leaderboard_chart()

# def fetch_executive_data(executive: str):
#     name = executive.capitalize()
#     try:
#         with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT cash_balance, stock_holdings, portfolio_value_history FROM corporate_ledgers WHERE executive = ?", (name,))
#             ledger_row = cursor.fetchone()
#             cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (name,))
#             inventory_row = cursor.fetchone()
#             cursor.execute("SELECT timestamp, log_type, message FROM system_logs WHERE executive = ? ORDER BY id DESC LIMIT 15", (name,))
#             log_rows = cursor.fetchall()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])
#     except Exception:
#         return "$0.00", pd.DataFrame(), pd.DataFrame(), "Syncing...", go.Figure()

#     if not ledger_row or not inventory_row:
#         return "$0.00", pd.DataFrame(), pd.DataFrame(), "Initializing...", go.Figure()

#     cash, holdings, history = ledger_row[0], json.loads(ledger_row[1]), json.loads(ledger_row[2])
#     raw_units, finished_units = inventory_row[0], inventory_row[1]

#     holdings_data = []
#     equity_value = 0.0
#     for symbol, qty in holdings.items():
#         unit_p = prices.get(symbol, 100.0)
#         tot_val = unit_p * qty; equity_value += tot_val
#         holdings_data.append({"Asset Ticker": symbol, "Shares Owned": qty, "Live Share Price": f"${unit_p:.2f}", "Total Net Value": f"${tot_val:.2f}"})

#     holdings_df = pd.DataFrame(holdings_data if holdings_data else [{"Asset Ticker": "NONE", "Shares Owned": 0, "Live Share Price": "$0.00", "Total Net Value": "$0.00"}])
#     inventory_df = pd.DataFrame([{"Resource Class": "📦 Raw Materials ($50/unit)", "Stock Volume": f"{raw_units} Units"}, {"Resource Class": "🛠️ Factory Finished Products", "Stock Volume": f"{finished_units} Units"}])

#     current_total_worth = cash + equity_value + (raw_units * prices.get("RAW_COST", 50.0))
#     current_time = datetime.now().strftime("%H:%M:%S")

#     history.append({"time": current_time, "worth": current_total_worth})
#     if len(history) > 25: history.pop(0)

#     with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#         conn.cursor().execute("UPDATE corporate_ledgers SET portfolio_value_history = ? WHERE executive = ?", (json.dumps(history), name))
#         conn.commit()

#     history_df = pd.DataFrame(history)
#     fig = go.Figure()
#     if not history_df.empty and "time" in history_df.columns:
#         fig.add_trace(go.Scatter(x=history_df["time"], y=history_df["worth"], mode="lines+markers", line=dict(color="#2b6cb0", width=3.5), marker=dict(color="#3182ce", size=6)))
#     fig.update_layout(title=f"{name} Value History Curve", paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc", font_color="#2d3748", title_font_color="#1a365d", margin=dict(l=40, r=30, t=40, b=40))

#     log_html = ""
#     for r in reversed(log_rows):
#         color = "#e53e3e" if r[1].upper() == "ERROR" else ("#2b6cb0" if r[1].upper() == "THOUGHT" else "#4a5568")
#         log_html += f"<div><b style='color:{color};'>[{r[0]}] {r[1].upper()}:</b> {r[2].replace('\n', '<br>')}</div>"

#     return f"${current_total_worth:,.2f}", holdings_df, inventory_df, log_html if log_html else "Waiting...", fig


# async def handle_executive_chat(name, user_message, history):
#     if not user_message:
#         return "", history

#     name = name.capitalize()
#     try:
#         with sqlite3.connect(DB_FILE) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT cash_balance, stock_holdings FROM corporate_ledgers WHERE executive = ?", (name,))
#             ledg = cursor.fetchone()
#             cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (name,))
#             inven = cursor.fetchone()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])
            
#         context_string = (
#             f"Your current live corporate state balances are: "
#             f"Cash Balance: ${ledg[0]:,.2f} USD. "
#             f"Stock Portfolio Units: {ledg[1]}. "
#             f"Raw Materials: {inven[0]} units. "
#             f"Finished Factory Products: {inven[1]} units. "
#             f"Shared Exchange Ticker Prices are currently: {prices}."
#         )
#     except Exception:
#         context_string = "Data bridge busy. Proceed with general corporate logic parameters."

#     personas = {
#         "Warren": "You are Warren, the Chief Value Officer. You are conservative, risk-averse, hate debt, value heavy liquidity cushions, and prefer holding defensive blue-chips like Apple (AAPL). Reply briefly, cleanly, and with wise investment tone.",
#         "George": "You are George, the Chief Macro Hedger. You are aggressive, tactical, watch macroeconomic indicators, and gladly liquidate assets into pure cash hoards to catch major market dips. Speak decisively and confidently.",
#         "Ray": "You are Ray, the Chief Diversification Officer. You follow mathematical risk parity rules. You insist on keeping an exactly even split exposure across all sectors (AAPL, TSLA, NVDA, AMZN) to avoid volatility shocks. Speak logically and analytically.",
#         "Cathie": "You are Cathie, the Chief Innovation Director. You are hyper-aggressive, hold zero cash buffers, run a lean supply chain layout, and dump every single dollar into disruptive innovation vectors like Tesla (TSLA) stock. Speak with fast-paced, high-energy tech-disruption optimism."
#     }

#     system_prompt = (
#         f"{personas.get(name, 'You are an AI corporate executive officer.')}\n\n"
#         f"CONTEXT CRITERIA: {context_string}\n\n"
#         f"INSTRUCTION: Answer the user question accurately using your live metrics. Stay completely in character. Keep answers under 3-4 sentences."
#     )

#     try:
#         response = await openrouter_client.chat.completions.create(
#             model="openai/gpt-oss-120b:free",
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_message}
#             ],
#             max_tokens=200,
#             temperature=0.7
#         )
#         ai_reply = response.choices[0].message.content
#     except Exception:
#         fallback_messages = {
#             "Warren": "This is Warren. Our corporate communication lines are processing heavy global transaction volume. My strategic focus remains cautious—please review our asset tables while the network data lines settle.",
#             "George": "George here. The macro data pipeline is hitting an upstream routing bottleneck at this moment. I am locking our capital securely in pure liquid cash until the lane clears. Stand by.",
#             "Ray": "Ray here. High public traffic on the server gateways has caused a temporary interface delay. Our risk-parity asset distribution remains perfectly balanced in the SQL database.",
#             "Cathie": "Cathie here! We are hitting a high-velocity surge on the network routing pools, but our disruptive innovation track doesn't sleep! Check our active growth vectors on the chart below while the lines speed up!"
#         }
#         ai_reply = fallback_messages.get(name, "Corporate data bridge busy. Balance sheets are secure. Please repeat your query shortly.")

#     history.append({"role": "user", "content": user_message})
#     history.append({"role": "assistant", "content": ai_reply})
#     return "", history


# # ==========================================
# # 🚀 FIXED: MULTI-AGENT BOARDROOM DEBATE LAYER (ASYNC GENERATOR)
# # ==========================================
# async def run_boardroom_debate(user_prompt, history):
#     if not user_prompt:
#         return  # ✅ FIXED: Bare return used to exit an async generator safely

#     history.append({"role": "user", "content": f"📋 BOARDROOM PROMPT: {user_prompt}"})
#     yield "", history

#     executives = ["George", "Warren", "Cathie", "Ray"]
    
#     # Run sequential inference so each agent builds on top of the last agent's analysis!
#     for exec_name in executives:
#         _, single_history = await handle_executive_chat(exec_name, user_prompt, [])
#         agent_response = single_history[1]["content"] if len(single_history) > 1 else "Analyzing operational vectors..."
        
#         history.append({
#             "role": "assistant", 
#             "content": f"👔 **{exec_name} ({'Chief Macro Hedger' if exec_name=='George' else 'Chief Value Officer' if exec_name=='Warren' else 'Chief Innovation Dir' if exec_name=='Cathie' else 'Chief Diversification Officer'}):**\n{agent_response}"
#         })
#         yield "", history
    
#     yield "", history  # ✅ FIXED: Final status yield sequence complete


# # ==========================================
# # 🛠️ MACRO CONTROL SHOCK EVENT ENGINE
# # ==========================================
# def trigger_market_shock_event(event_type: str):
#     try:
#         with sqlite3.connect(DB_FILE) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])

#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             details = ""

#             if event_type == "crash":
#                 prices["AAPL"] = round(prices["AAPL"] * 0.75, 2)
#                 prices["TSLA"] = round(prices["TSLA"] * 0.70, 2)
#                 prices["NVDA"] = round(prices["NVDA"] * 0.65, 2)
#                 prices["AMZN"] = round(prices["AMZN"] * 0.75, 2)
#                 details = "📉 BLACK THURSDAY: Simulated Equity Market Crash triggered (-25% Tickers)."
#             elif event_type == "rally":
#                 prices["AAPL"] = round(prices["AAPL"] * 1.25, 2)
#                 prices["TSLA"] = round(prices["TSLA"] * 1.30, 2)
#                 prices["NVDA"] = round(prices["NVDA"] * 1.40, 2)
#                 prices["AMZN"] = round(prices["AMZN"] * 1.20, 2)
#                 details = "🚀 TECH BULL RALLY: Global liquidity influx forced sudden hyper-asset evaluation growth."
#             elif event_type == "supply":
#                 prices["RAW_COST"] = round(prices["RAW_COST"] * 1.80, 2)
#                 prices["RETAIL_VALUE"] = round(prices["RETAIL_VALUE"] * 0.85, 2)
#                 details = "📦 SUPPLY CHAIN SHOCK: Material costs increased 80%; consumer demand dropped retail velocity margins."

#             cursor.execute("UPDATE global_market_state SET value_data = ? WHERE key = 'prices'", (json.dumps(prices),))
#             cursor.execute("INSERT INTO security_audit_vault (timestamp, executive, action_type, details) VALUES (?, 'SYSTEM', 'MACRO_SHOCK', ?)", (timestamp, details))
            
#             # Write global alert logs to all executive boards
#             for ex in ["Warren", "George", "Ray", "Cathie"]:
#                 cursor.execute("INSERT INTO system_logs (executive, timestamp, log_type, message) VALUES (?, datetime('now'), 'ERROR', ?)", (ex, details))
                
#             conn.commit()
#             return f"Success: {details}"
#     except Exception as e:
#         return f"Shock Controller Malfunction: {e}"


# def build_executive_tab(name: str):
#     with gr.Tab(name, elem_classes="tabs"):
#         with gr.Row():
#             # Left Panel: Balance Sheet Metrics
#             with gr.Column(scale=2):
#                 worth_display = gr.Textbox(label="Unified Net Asset Valuation (USD)", value="$10,000.00", interactive=False, elem_classes="stat-box")
#                 gr.Markdown("### 📈 Active Equity Allocations")
#                 holdings_table = gr.Dataframe(interactive=False)
#                 gr.Markdown("### 🏭 Warehouse Physical Freight Stack")
#                 inventory_table = gr.Dataframe(interactive=False)
#                 chart_display = gr.Plot()
                
#             # Right Panel: Dedicated Chat Interface
#             with gr.Column(scale=3):
#                 gr.Markdown(f"### 💬 Dedicated Interview Terminal: CFO {name}")
#                 chat_interface = gr.Chatbot(height=350, label=f"Secure {name} Connection Line", type="messages")
#                 with gr.Row():
#                     chat_input = gr.Textbox(placeholder=f"Ask Executive {name} about their current balance sheet...", show_label=False, scale=4)
#                     send_btn = gr.Button("SEND", variant="primary", scale=1)
                
#                 example_questions = {
#                     "Warren": [["Warren, do you think our strategy is too safe?"], ["Warren, what is your favorite stock to buy?"]],
#                     "George": [["George, what are you doing with our cash right now?"], ["Why shouldn't we buy stocks today, George?"]],
#                     "Ray": [["Ray, how are you keeping our portfolio balanced?"], ["Ray, explain your mathematical risk-parity approach."]],
#                     "Cathie": [["Cathie, are you going to dump our capital into TSLA?"], ["Why do you run such a thin cash reserve cushion?"]]
#                 }
                
#                 gr.Examples(
#                     examples=example_questions.get(name, []),
#                     inputs=[chat_input],
#                     label="💡 Click a suggested strategic question to ask this executive:"
#                 )
        
#         gr.Markdown("### Sat-Link Operational Activity Feed & Strategy Thoughts")
#         console_markdown = gr.HTML(value="Initializing...", elem_classes="scroll-feed-container")
        
#         send_btn.click(
#             fn=handle_executive_chat, 
#             inputs=[gr.State(name), chat_input, chat_interface], 
#             outputs=[chat_input, chat_interface]
#         )
#         chat_input.submit(
#             fn=handle_executive_chat, 
#             inputs=[gr.State(name), chat_input, chat_interface], 
#             outputs=[chat_input, chat_interface]
#         )
        
#         app.load(fn=lambda: fetch_executive_data(name), outputs=[worth_display, holdings_table, inventory_table, console_markdown, chart_display])
#         refresh_timer = gr.Timer(value=2.0)
#         refresh_timer.tick(fn=lambda: fetch_executive_data(name), outputs=[worth_display, holdings_table, inventory_table, console_markdown, chart_display], show_progress="hidden", queue=False)


# with gr.Blocks(css=premium_light_css, js=force_light_js) as app:
#     with gr.Row(elem_id="master-header"):
#         with gr.Column(): 
#             gr.Markdown("# 🎓 Titan Corporate Executive Network — Multi-Agent System")

#     with gr.Row():
#         with gr.Column():
#             leaderboard_plot = gr.Plot(value=fetch_global_leaderboard_chart())

#     with gr.Row():
#         # Exchange Board Left Column
#         with gr.Column(scale=2):
#             gr.Markdown("### 🌐 Live Shared Exchange Stock Tickers")
#             market_table = gr.Dataframe(interactive=False)
            
#             # MACRO SHOCK CONTROL DOCK
#             gr.Markdown("### 🚨 Macro System Shock Event Injector")
#             with gr.Row():
#                 btn_crash = gr.Button("🚨 TRIGGER EQUITY MARKET CRASH (-25%)", variant="stop", elem_classes="control-btn")
#                 btn_rally = gr.Button("🚀 INJECT HYPER TECH BULL RALLY (+30%)", variant="primary", elem_classes="control-btn")
#             btn_supply = gr.Button("📦 SIMULATE SUPPLY CHAIN CRISIS (+80% RAW COSTS)", variant="secondary", elem_classes="control-btn")
            
#             shock_status = gr.Textbox(label="Last Executed System Shock Log Event", value="No macro override actions logged in this run window.", interactive=False)
            
#             btn_crash.click(fn=lambda: trigger_market_shock_event("crash"), outputs=[shock_status])
#             btn_rally.click(fn=lambda: trigger_market_shock_event("rally"), outputs=[shock_status])
#             btn_supply.click(fn=lambda: trigger_market_shock_event("supply"), outputs=[shock_status])

#         # Security Ledger Audit Trail Right Column
#         with gr.Column(scale=3):
#             gr.Markdown("### 🔒 Secure Verification Ledger Audit Trail Checkpoints")
#             vault_table = gr.Dataframe(interactive=False)

#     # Render independent executive tabs
#     build_executive_tab("Warren")
#     build_executive_tab("George")
#     build_executive_tab("Ray")
#     build_executive_tab("Cathie")

#     # JOINT BOARDROOM DEBATE CHAMBER
#     with gr.Tab("👔 Shared Boardroom Consensus Chamber", elem_classes="tabs"):
#         gr.Markdown("### 🏛️ Joint Executive Council Debate Forum")
#         gr.Markdown("Submit a major strategic decision or corporate query below. All 4 executives will evaluate it sequentially based on their live database parameters and debate the optimal outcome!")
        
#         board_chatbot = gr.Chatbot(height=450, label="Live Executive Cross-Examination Feed", type="messages")
#         with gr.Row():
#             board_input = gr.Textbox(placeholder="Enter a strategic proposal (e.g., 'Should we expand raw storage inventory or buy tech equities today?')...", show_label=False, scale=4)
#             board_send = gr.Button("CONVENE BOARDROOM COUNCIL", variant="primary", scale=1)
            
#         board_examples = gr.Examples(
#             examples=[
#                 ["Should we completely liquidate our stock holdings and shift to pure cash buffers today?"],
#                 ["Given our current $10,000 baseline, is scaling factory raw materials better than buying NVDA/TSLA?"]
#             ],
#             inputs=[board_input],
#             label="💡 Click a boardroom dilemma sample to run the multi-agent consensus script:"
#         )
        
#         board_send.click(fn=run_boardroom_debate, inputs=[board_input, board_chatbot], outputs=[board_input, board_chatbot])
#         board_input.submit(fn=run_boardroom_debate, inputs=[board_input, board_chatbot], outputs=[board_input, board_chatbot])

#     global_timer = gr.Timer(value=2.0)
#     global_timer.tick(fn=fetch_global_market_status, outputs=[market_table, vault_table, leaderboard_plot], show_progress="hidden", queue=False)

# if __name__ == "__main__":
#     # app.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
#     app.launch()





# # Gradio Deployed code

# import gradio as gr
# import sqlite3
# import json
# import pandas as pd
# import plotly.graph_objects as go
# from datetime import datetime
# from openai import AsyncOpenAI
# import os
# import asyncio
# import threading
# import time
# from dotenv import load_dotenv

# DB_FILE = "titan_corp.db"

# # Initialize environment variables safely
# load_dotenv()

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# openrouter_client = AsyncOpenAI(
#     base_url="https://openrouter.ai/api/v1", 
#     api_key=OPENROUTER_API_KEY
# )

# # ==========================================
# # 🚀 AUTOMATED BACKGROUND WORKER ACTIVATION
# # ==========================================
# # This background thread automatically runs your exact 'titan_floor.py' trading logic 
# # directly inside the Hugging Face space container so your agents trade 24/7!
# def start_trading_floor():
#     try:
#         import titan_floor
#         # If your titan_floor has a main loop function, we can trigger it.
#         # Otherwise, importing it executes your file's background script blocks perfectly.
#         if hasattr(titan_floor, "main"):
#             titan_floor.main()
#     except Exception as e:
#         print(f"Trading Floor Background Worker Status: {e}")

# # Fire up your titan_floor file cleanly inside an independent thread when app.py starts
# threading.Thread(target=start_trading_floor, daemon=True).start()


# # 💎 PREMIUM HIGH-CONTRAST LIGHT PLATINUM THEME (ZERO BLACK OVERRIDES ALLOWED)
# premium_light_css = """
# /* 🔴 SYSTEM RESET: Force the application frame to consume 100% of screen width */
# body, html, .gradio-container, .main, #root { 
#     max-width: 100% !important; 
#     width: 100% !important; 
#     padding: 0 !important; 
#     margin: 0 !important; 
#     background-color: #f4f6f9 !important; 
# }

# /* 🏢 HEADER RESETS */
# #master-header { 
#     text-align: center; 
#     border-bottom: 4px solid #1a365d; 
#     padding: 15px 10px !important; 
#     margin-bottom: 15px; 
#     background: #ffffff !important; 
#     box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
# }
# #master-header h1 { color: #1a365d !important; margin: 0; font-weight: 700; font-size: 2rem; text-transform: uppercase; }

# /* 📋 HIGH-VISIBILITY CONTROLS FOR TABS AND TEXT */
# .tabs { background: #ffffff !important; border: 1px solid #cbd5e0 !important; border-radius: 8px !important; }
# .tab-nav { border-bottom: 3px solid #cbd5e0 !important; background: #edf2f7 !important; display: flex !important; }
# .tab-nav button { font-weight: 700 !important; color: #2d3748 !important; padding: 12px 24px !important; background: transparent !important; }
# .tab-nav button.selected { border-bottom: 4px solid #3182ce !important; color: #1a365d !important; background: #ffffff !important; }

# /* 🔴 ERADICATE BLACK COLOR ENTIRELY FROM CHATBOTS, DATAFRAMES, TEXTBOXES, AND INTERFACES */
# .block, .gradio-dataframe, .gradio-chatbot, table, tr, td, th, .form, .table-wrap, .form-row, .card, .bubble, .user, .bot {
#     background-color: #ffffff !important; 
#     background: #ffffff !important;
#     border-color: #cbd5e0 !important;
# }

# /* FORCE HIGH-CONTRAST DARK BLUE METRIC FONTS ON EVERYTHING FOR FULL READABILITY */
# span, p, h1, h2, h3, label, th, td, button, .m-12, div, .label, .group, .md { 
#     color: #1a365d !important; 
#     font-weight: 600 !important; 
# }

# input, textarea, .primary, .secondary, [class*="form-text-input"], div[data-testid="block-info"] {
#     background-color: #ffffff !important;
#     background: #ffffff !important;
#     color: #1a365d !important;
#     border: 1px solid #cbd5e0 !important;
# }

# /* ⚡ SYNCED HORIZONTAL GRID FORCING SIDE-BY-SIDE PANELS LIKE LOCAL MONITOR SCREEN */
# .main-dashboard-grid { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 20px !important; width: 100% !important; padding: 0 15px !important; }
# .dashboard-left-pane { flex: 5 !important; min-width: 0 !important; }
# .dashboard-right-pane { flex: 5 !important; min-width: 0 !important; }

# .executive-row-grid { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 20px !important; width: 100% !important; }
# .executive-left-col { flex: 4.8 !important; min-width: 0 !important; }
# .executive-right-col { flex: 5.2 !important; min-width: 0 !important; }

# /* HEIGHT CONSTRAINTS */
# .executive-chatbot-window { height: 420px !important; background-color: #ffffff !important; }
# .scroll-feed-container { background-color: #f8fafc !important; border: 1px solid #cbd5e0 !important; border-radius: 6px !important; padding: 15px !important; height: 160px !important; overflow-y: scroll !important; }
# .scroll-feed-container div { border-bottom: 1px dashed #cbd5e0; padding-bottom: 6px; margin-bottom: 8px; font-size: 13.5px; color: #1a365d !important; }
# .stat-box { background: #ebf8ff !important; border-left: 5px solid #3182ce !important; }
# .control-btn { font-weight: bold !important; border-radius: 6px !important; background-color: #edf2f7 !important; }
# footer { visibility: hidden !important; display: none !important; }
# """

# force_light_js = "function() { const url = new URL(window.location); if (url.searchParams.get('__theme') !== 'light') { url.searchParams.set('__theme', 'light'); window.location.href = url.href; } }"

# IS_SPACE = "SPACE_ID" in os.environ

# def fetch_global_leaderboard_chart():
#     executives = ["Warren", "George", "Ray", "Cathie"]
#     colors = {"Warren": "#2b6cb0", "George": "#4a5568", "Ray": "#2f855a", "Cathie": "#dd6b20"}
#     fig = go.Figure()
#     try:
#         with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#             cursor = conn.cursor()
#             for name in executives:
#                 cursor.execute("SELECT portfolio_value_history FROM corporate_ledgers WHERE executive = ?", (name,))
#                 row = cursor.fetchone()
#                 if row and row[0]:
#                     history = json.loads(row[0])
#                     if history:
#                         df = pd.DataFrame(history)
#                         if not df.empty and "time" in df.columns:
#                             fig.add_trace(go.Scatter(
#                                 x=df["time"], y=df["worth"], mode="lines+markers",
#                                 name=f"CFO {name}", line=dict(color=colors[name], width=3), marker=dict(size=5)
#                             ))
#     except Exception:
#         pass
#     fig.update_layout(
#         paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc", font_color="#2d3748", title_font_color="#1a365d",
#         margin=dict(l=40, r=30, t=30, b=30), xaxis=dict(gridcolor="#e2e8f0"), yaxis=dict(gridcolor="#e2e8f0")
#     )
#     return fig

# def fetch_global_market_status():
#     try:
#         with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])
#             cursor.execute("SELECT timestamp, executive, action_type, details FROM security_audit_vault ORDER BY id DESC LIMIT 5")
#             vault_rows = cursor.fetchall()
#     except Exception:
#         return pd.DataFrame(), pd.DataFrame(), fetch_global_leaderboard_chart()

#     ticker_df = pd.DataFrame([{"Asset Ticker": k, "Exchange Price / Cost": f"${v:,.2f}"} for k, v in prices.items()])
#     vault_df = pd.DataFrame([{"Timestamp": r[0], "Executive Officer": r[1], "Verified Corporate Action": r[3], "Status": "✅ VERIFIED"} for r in vault_rows] if vault_rows else [{"Timestamp": "-", "Executive Officer": "-", "Verified Corporate Action": "Awaiting operations...", "Status": "-"}])
#     return ticker_df, vault_df, fetch_global_leaderboard_chart()

# def fetch_executive_data(executive: str):
#     name = executive.capitalize()
#     try:
#         with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT cash_balance, stock_holdings, portfolio_value_history FROM corporate_ledgers WHERE executive = ?", (name,))
#             ledger_row = cursor.fetchone()
#             cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (name,))
#             inventory_row = cursor.fetchone()
#             cursor.execute("SELECT timestamp, log_type, message FROM system_logs WHERE executive = ? ORDER BY id DESC LIMIT 10", (name,))
#             log_rows = cursor.fetchall()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])
#     except Exception:
#         return "$0.00", pd.DataFrame(), pd.DataFrame(), "Syncing...", go.Figure()

#     if not ledger_row or not inventory_row:
#         return "$0.00", pd.DataFrame(), pd.DataFrame(), "Initializing...", go.Figure()

#     cash, holdings, history = ledger_row[0], json.loads(ledger_row[1]), json.loads(ledger_row[2])
#     raw_units, finished_units = inventory_row[0], inventory_row[1]

#     holdings_data = []
#     equity_value = 0.0
#     for symbol, qty in holdings.items():
#         unit_p = prices.get(symbol, 100.0)
#         tot_val = unit_p * qty; equity_value += tot_val
#         holdings_data.append({"Asset Ticker": symbol, "Shares Owned": qty, "Live Share Price": f"${unit_p:.2f}", "Total Net Value": f"${tot_val:.2f}"})

#     holdings_df = pd.DataFrame(holdings_data if holdings_data else [{"Asset Ticker": "NONE", "Shares Owned": 0, "Live Share Price": "$0.00", "Total Net Value": "$0.00"}])
#     inventory_df = pd.DataFrame([{"Resource Class": "📦 Raw Materials ($50/unit)", "Stock Volume": f"{raw_units} Units"}, {"Resource Class": "🛠️ Factory Finished Products", "Stock Volume": f"{finished_units} Units"}])

#     current_total_worth = cash + equity_value + (raw_units * prices.get("RAW_COST", 50.0))
#     current_time = datetime.now().strftime("%H:%M:%S")

#     history.append({"time": current_time, "worth": current_total_worth})
#     if len(history) > 25: history.pop(0)

#     with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#         conn.cursor().execute("UPDATE corporate_ledgers SET portfolio_value_history = ? WHERE executive = ?", (json.dumps(history), name))
#         conn.commit()

#     history_df = pd.DataFrame(history)
#     fig = go.Figure()
#     if not history_df.empty and "time" in history_df.columns:
#         fig.add_trace(go.Scatter(x=history_df["time"], y=history_df["worth"], mode="lines+markers", line=dict(color="#2b6cb0", width=3.5), marker=dict(color="#3182ce", size=6)))
#     fig.update_layout(paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc", font_color="#2d3748", title_font_color="#1a365d", margin=dict(l=40, r=30, t=30, b=30))

#     log_html = ""
#     for r in reversed(log_rows):
#         color = "#e53e3e" if r[1].upper() == "ERROR" else ("#2b6cb0" if r[1].upper() == "THOUGHT" else "#4a5568")
#         log_html += f"<div><b style='color:{color};'>[{r[0]}] {r[1].upper()}:</b> {r[2].replace('\n', '<br>')}</div>"

#     return f"${current_total_worth:,.2f}", holdings_df, inventory_df, log_html if log_html else "Waiting...", fig


# async def handle_executive_chat(name, user_message, history):
#     if not user_message:
#         return "", history

#     name = name.capitalize()
#     try:
#         with sqlite3.connect(DB_FILE) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT cash_balance, stock_holdings FROM corporate_ledgers WHERE executive = ?", (name,))
#             ledg = cursor.fetchone()
#             cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (name,))
#             inven = cursor.fetchone()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])
            
#         context_string = f"Cash: ${ledg[0]:,.2f}, Stocks: {ledg[1]}, Raw: {inven[0]}, Finished: {inven[1]}."
#     except Exception:
#         context_string = "Baseline corporate metrics active."

#     personas = {
#         "Warren": "You are Warren, the Chief Value Officer. Conservative, risk-averse, prefer Apple (AAPL). Under 3 sentences.",
#         "George": "You are George, the Chief Macro Hedger. Aggressive, move assets to liquid cash buffers on spikes. Under 3 sentences.",
#         "Ray": "You are Ray, the Chief Diversification Officer. Strict mathematical risk parity split exposure. Under 3 sentences.",
#         "Cathie": "You are Cathie, the Chief Innovation Director. Hyper-aggressive growth vectors, load Tesla (TSLA) stock. Under 3 sentences."
#     }

#     system_prompt = f"{personas.get(name, 'Executive AI')}\nMetrics: {context_string}"

#     try:
#         response = await openrouter_client.chat.completions.create(
#             model="openai/gpt-oss-120b:free",
#             messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_message}],
#             max_tokens=150, temperature=0.7
#         )
#         ai_reply = response.choices[0].message.content
#     except Exception:
#         ai_reply = "Secure executive data line stable. State parameters synchronized."

#     history.append({"role": "user", "content": user_message})
#     history.append({"role": "assistant", "content": ai_reply})
#     return "", history


# async def run_boardroom_debate(user_prompt, history):
#     if not user_prompt:
#         return
#     history.append({"role": "user", "content": f"📋 BOARDROOM PROMPT: {user_prompt}"})
#     yield "", history
#     for exec_name in ["George", "Warren", "Cathie", "Ray"]:
#         _, single_history = await handle_executive_chat(exec_name, user_prompt, [])
#         agent_response = single_history[1]["content"] if len(single_history) > 1 else "Processing boardroom ledger context..."
#         history.append({"role": "assistant", "content": f"👔 **{exec_name}:** {agent_response}"})
#         yield "", history


# def trigger_market_shock_event(event_type: str):
#     try:
#         with sqlite3.connect(DB_FILE) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#             prices = json.loads(cursor.fetchone()[0])
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             details = ""

#             if event_type == "crash":
#                 prices["AAPL"] = round(prices["AAPL"] * 0.75, 2)
#                 prices["TSLA"] = round(prices["TSLA"] * 0.70, 2)
#                 prices["NVDA"] = round(prices["NVDA"] * 0.65, 2)
#                 prices["AMZN"] = round(prices["AMZN"] * 0.75, 2)
#                 details = "📉 BLACK THURSDAY: Simulated Equity Market Crash triggered (-25% Tickers)."
#             elif event_type == "rally":
#                 prices["AAPL"] = round(prices["AAPL"] * 1.25, 2)
#                 prices["TSLA"] = round(prices["TSLA"] * 1.30, 2)
#                 prices["NVDA"] = round(prices["NVDA"] * 1.40, 2)
#                 prices["AMZN"] = round(prices["AMZN"] * 1.20, 2)
#                 details = "🚀 TECH BULL RALLY: Global liquidity influx forced sudden hyper-asset evaluation growth."
#             elif event_type == "supply":
#                 prices["RAW_COST"] = round(prices["RAW_COST"] * 1.80, 2)
#                 prices["RETAIL_VALUE"] = round(prices["RETAIL_VALUE"] * 0.85, 2)
#                 details = "📦 SUPPLY CHAIN SHOCK: Material costs increased 80%; consumer demand dropped retail velocity margins."

#             cursor.execute("UPDATE global_market_state SET value_data = ? WHERE key = 'prices'", (json.dumps(prices),))
#             cursor.execute("INSERT INTO security_audit_vault (timestamp, executive, action_type, details) VALUES (?, 'SYSTEM', 'MACRO_SHOCK', ?)", (timestamp, details))
#             for ex in ["Warren", "George", "Ray", "Cathie"]:
#                 cursor.execute("INSERT INTO system_logs (executive, timestamp, log_type, message) VALUES (?, datetime('now'), 'ERROR', ?)", (ex, details))
#             conn.commit()
#             return f"Success: {details}"
#     except Exception as e:
#         return f"Shock Controller Malfunction: {e}"


# # ==========================================
# # 🧱 MAIN GRADIO BLOCKS APPLICATION PORTAL
# # ==========================================
# with gr.Blocks(css=premium_light_css, js=force_light_js) as app:
#     with gr.Row(elem_id="master-header"):
#         with gr.Column(): 
#             gr.Markdown("# 🎓 Titan Corporate Executive Network — Multi-Agent System")

#     with gr.Row():
#         with gr.Column():
#             leaderboard_plot = gr.Plot(value=fetch_global_leaderboard_chart())

#     with gr.Row(elem_classes="main-dashboard-grid"):
#         with gr.Column(elem_classes="dashboard-left-pane"):
#             gr.Markdown("### 🌐 Live Shared Exchange Stock Tickers")
#             market_table = gr.Dataframe(interactive=False)
            
#             gr.Markdown("### 🚨 Macro System Shock Event Injector")
#             with gr.Row():
#                 btn_crash = gr.Button("🚨 TRIGGER EQUITY MARKET CRASH (-25%)", variant="stop", elem_classes="control-btn")
#                 btn_rally = gr.Button("🚀 INJECT HYPER TECH BULL RALLY (+30%)", variant="primary", elem_classes="control-btn")
#             btn_supply = gr.Button("📦 SIMULATE SUPPLY CHAIN CRISIS (+80% RAW COSTS)", variant="secondary", elem_classes="control-btn")
#             shock_status = gr.Textbox(label="Last Executed System Shock Log Event", value="No macro override actions logged in this run window.", interactive=False)

#         with gr.Column(elem_classes="dashboard-right-pane"):
#             gr.Markdown("### 🔒 Secure Verification Ledger Audit Trail Checkpoints")
#             vault_table = gr.Dataframe(interactive=False)

#     # Predefined pools for suggested queries mapped to every tab natively
#     example_pools = {
#         "Warren": [["Warren, do you think our strategy is too safe?"], ["Warren, what is your favorite stock to buy?"]],
#         "George": [["George, what are you doing with our cash right now?"], ["Why shouldn't we buy stocks today, George?"]],
#         "Ray": [["Ray, how are you keeping our portfolio balanced?"], ["Ray, explain your mathematical risk-parity approach."]],
#         "Cathie": [["Cathie, are you going to dump our capital into TSLA?"], ["Why do you run such a thin cash reserve cushion?"]]
#     }

#     # Render independent executive views
#     for name in ["Warren", "George", "Ray", "Cathie"]:
#         with gr.Tab(name, elem_classes="tabs"):
#             with gr.Row(elem_classes="executive-row-grid"):
#                 with gr.Column(elem_classes="executive-left-col"):
#                     worth_display = gr.Textbox(label="Unified Net Asset Valuation (USD)", value="$10,000.00", interactive=False, elem_classes="stat-box")
#                     gr.Markdown("### 📈 Active Equity Allocations")
#                     holdings_table = gr.Dataframe(interactive=False)
#                     gr.Markdown("### 🏭 Warehouse Physical Freight Stack")
#                     inventory_table = gr.Dataframe(interactive=False)
#                     chart_display = gr.Plot()
                    
#                 with gr.Column(elem_classes="executive-right-col"):
#                     gr.Markdown(f"### 💬 Dedicated Interview Terminal: CFO {name}")
#                     chat_interface = gr.Chatbot(label=f"Secure {name} Connection Line", elem_classes="executive-chatbot-window")
#                     with gr.Row():
#                         chat_input = gr.Textbox(placeholder=f"Ask Executive {name} about their current balance sheet...", show_label=False, scale=4)
#                         send_btn = gr.Button("SEND", variant="primary", scale=1)
                    
#                     # ✅ FIXED: Now binds specific question suggestions across all tabs natively
#                     gr.Examples(examples=example_pools[name], inputs=[chat_input], label="💡 Suggested strategic questions:")
            
#             gr.Markdown("### Sat-Link Operational Activity Feed & Strategy Thoughts")
#             console_markdown = gr.HTML(value="Initializing...", elem_classes="scroll-feed-container")
            
#             send_btn.click(fn=handle_executive_chat, inputs=[gr.State(name), chat_input, chat_interface], outputs=[chat_input, chat_interface])
#             chat_input.submit(fn=handle_executive_chat, inputs=[gr.State(name), chat_input, chat_interface], outputs=[chat_input, chat_interface])
#             app.load(fn=lambda n=name: fetch_executive_data(n), outputs=[worth_display, holdings_table, inventory_table, console_markdown, chart_display])

#     with gr.Tab("👔 Shared Boardroom Consensus Chamber", elem_classes="tabs"):
#         gr.Markdown("### 🏛️ Joint Executive Council Debate Forum")
#         board_chatbot = gr.Chatbot(height=450, label="Live Executive Cross-Examination Feed")
#         with gr.Row():
#             board_input = gr.Textbox(placeholder="Enter a strategic proposal...", show_label=False, scale=4)
#             board_send = gr.Button("CONVENE COUNCIL", variant="primary", scale=1)
            
#         # ✅ FIXED: Boardroom examples now mapped safely to the interface column layer
#         gr.Examples(
#             examples=[
#                 ["Should we completely liquidate our stock holdings and shift to pure cash buffers today?"],
#                 ["Given our current baseline, is scaling factory raw materials better than buying NVDA/TSLA?"]
#             ],
#             inputs=[board_input],
#             label="💡 Click a boardroom dilemma sample to run the multi-agent consensus script:"
#         )
#         board_send.click(fn=run_boardroom_debate, inputs=[board_input, board_chatbot], outputs=[board_input, board_chatbot])
#         board_input.submit(fn=run_boardroom_debate, inputs=[board_input, board_chatbot], outputs=[board_input, board_chatbot])

#     btn_crash.click(fn=lambda: trigger_market_shock_event("crash"), outputs=[shock_status])
#     btn_rally.click(fn=lambda: trigger_market_shock_event("rally"), outputs=[shock_status])
#     btn_supply.click(fn=lambda: trigger_market_shock_event("supply"), outputs=[shock_status])

#     # Dynamic layout refresh interface
#     global_timer = gr.Timer(value=3.0)
#     global_timer.tick(fn=fetch_global_market_status, outputs=[market_table, vault_table, leaderboard_plot], show_progress="hidden", queue=False)

# if __name__ == "__main__":
#     app.launch()



# Github develpoed code

import gradio as gr
import sqlite3
import json
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from openai import AsyncOpenAI
import os
import asyncio
import threading
from dotenv import load_dotenv

DB_FILE = "titan_corp.db"

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
openrouter_client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1", 
    api_key=OPENROUTER_API_KEY
)

# 🌐 NATIVE CLOUD BACKGROUND RUNNER THREAD
def start_floor_thread():
    try:
        import titan_floor
        import asyncio
        # Safely calls your floor script main automation loop inside memory
        asyncio.run(titan_floor.main_automation_loop())
    except Exception as e:
        print(f"Trading Floor Background Process Engine Status: {e}")

threading.Thread(target=start_floor_thread, daemon=True).start()

# 💎 PREMIUM FULL-WIDTH LIGHT THEME (ZERO BLACK CARD OVERRIDES ALLOWED)
premium_light_css = """
body, html, .gradio-container, .main, #root, .grid { 
    max-width: 100% !important; 
    width: 100% !important; 
    padding: 0 !important; 
    margin: 0 !important; 
    background-color: #f4f6f9 !important; 
}
#master-header { 
    text-align: center; 
    border-bottom: 4px solid #1a365d; 
    padding: 15px 10px !important; 
    margin-bottom: 15px; 
    background: #ffffff !important; 
    box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
}
#master-header h1 { color: #1a365d !important; margin: 0; font-weight: 700; font-size: 2rem; text-transform: uppercase; }

.tabs { background: #ffffff !important; border: 1px solid #cbd5e0 !important; border-radius: 8px !important; }
.tab-nav { border-bottom: 3px solid #cbd5e0 !important; background: #edf2f7 !important; display: flex !important; }
.tab-nav button { font-weight: 700 !important; color: #2d3748 !important; padding: 12px 24px !important; background: transparent !important; }
.tab-nav button.selected { border-bottom: 4px solid #3182ce !important; color: #1a365d !important; background: #ffffff !important; }

.block, .gradio-dataframe, .gradio-chatbot, table, tr, td, th, .form, .table-wrap, .form-row, .card, .bubble, .user, .bot {
    background-color: #ffffff !important; 
    background: #ffffff !important;
    border-color: #cbd5e0 !important;
}
span, p, h1, h2, h3, label, th, td, button, .m-12, div, .label, .group, .md { 
    color: #1a365d !important; 
    font-weight: 600 !important; 
}
input, textarea, .primary, .secondary, [class*="form-text-input"], div[data-testid="block-info"] {
    background-color: #ffffff !important;
    background: #ffffff !important;
    color: #1a365d !important;
    border: 1px solid #cbd5e0 !important;
}

.main-dashboard-grid { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 20px !important; width: 100% !important; padding: 0 15px !important; }
.dashboard-left-pane { flex: 5 !important; min-width: 0 !important; }
.dashboard-right-pane { flex: 5 !important; min-width: 0 !important; }

.executive-row-grid { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 20px !important; width: 100% !important; }
.executive-left-col { flex: 4.8 !important; min-width: 0 !important; }
.executive-right-col { flex: 5.2 !important; min-width: 0 !important; }

.executive-chatbot-window { height: 420px !important; background-color: #ffffff !important; }
.scroll-feed-container { background-color: #f8fafc !important; border: 1px solid #cbd5e0 !important; border-radius: 6px !important; padding: 15px !important; height: 160px !important; overflow-y: scroll !important; }
.scroll-feed-container div { border-bottom: 1px dashed #cbd5e0; padding-bottom: 6px; margin-bottom: 8px; font-size: 13.5px; color: #1a365d !important; }
.stat-box { background: #ebf8ff !important; border-left: 4px solid #3182ce !important; }
.control-btn { font-weight: bold !important; border-radius: 6px !important; background-color: #edf2f7 !important; }
footer { visibility: hidden !important; display: none !important; }
"""

force_light_js = "function() { const url = new URL(window.location); if (url.searchParams.get('__theme') !== 'light') { url.searchParams.set('__theme', 'light'); window.location.href = url.href; } }"

def fetch_global_leaderboard_chart():
    executives = ["Warren", "George", "Ray", "Cathie"]
    colors = {"Warren": "#2b6cb0", "George": "#4a5568", "Ray": "#2f855a", "Cathie": "#dd6b20"}
    fig = go.Figure()
    try:
        with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
            cursor = conn.cursor()
            for name in executives:
                cursor.execute("SELECT portfolio_value_history FROM corporate_ledgers WHERE executive = ?", (name,))
                row = cursor.fetchone()
                if row and row[0]:
                    history = json.loads(row[0])
                    if history:
                        df = pd.DataFrame(history)
                        if not df.empty and "time" in df.columns:
                            fig.add_trace(go.Scatter(
                                x=df["time"], y=df["worth"], mode="lines+markers",
                                name=f"CFO {name}", line=dict(color=colors[name], width=3), marker=dict(size=5)
                            ))
    except Exception:
        pass
    fig.update_layout(paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc", margin=dict(l=40, r=30, t=30, b=30), xaxis=dict(gridcolor="#e2e8f0"), yaxis=dict(gridcolor="#e2e8f0"))
    return fig

def fetch_global_market_status():
    try:
        with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
            prices = json.loads(cursor.fetchone()[0])
            cursor.execute("SELECT timestamp, executive, action_type, details FROM security_audit_vault ORDER BY id DESC LIMIT 5")
            vault_rows = cursor.fetchall()
    except Exception:
        return pd.DataFrame(), pd.DataFrame(), fetch_global_leaderboard_chart()
    ticker_df = pd.DataFrame([{"Asset Ticker": k, "Exchange Price / Cost": f"${v:,.2f}"} for k, v in prices.items()])
    vault_df = pd.DataFrame([{"Timestamp": r[0], "Executive Officer": r[1], "Verified Corporate Action": r[3], "Status": "✅ VERIFIED"} for r in vault_rows] if vault_rows else [{"Timestamp": "-", "Executive Officer": "-", "Verified Corporate Action": "Awaiting operations...", "Status": "-"}])
    return ticker_df, vault_df, fetch_global_leaderboard_chart()

def fetch_executive_data(name: str):
    try:
        with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT cash_balance, stock_holdings, portfolio_value_history FROM corporate_ledgers WHERE executive = ?", (name,))
            ledger_row = cursor.fetchone()
            cursor.execute("SELECT raw_material_units, finished_goods_units FROM supply_chain_inventory WHERE executive = ?", (name,))
            inventory_row = cursor.fetchone()
            cursor.execute("SELECT timestamp, log_type, message FROM system_logs WHERE executive = ? ORDER BY id DESC LIMIT 10", (name,))
            log_rows = cursor.fetchall()
            cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
            prices = json.loads(cursor.fetchone()[0])
    except Exception:
        return "$0.00", pd.DataFrame(), pd.DataFrame(), "Syncing...", go.Figure()

    if not ledger_row or not inventory_row:
        return "$0.00", pd.DataFrame(), pd.DataFrame(), "Initializing...", go.Figure()

    cash, holdings, history = ledger_row[0], json.loads(ledger_row[1]), json.loads(ledger_row[2])
    raw_units, finished_units = inventory_row[0], inventory_row[1]

    holdings_data = []
    equity_value = 0.0
    for symbol, qty in holdings.items():
        unit_p = prices.get(symbol, 100.0)
        tot_val = unit_p * qty; equity_value += tot_val
        holdings_data.append({"Asset Ticker": symbol, "Shares Owned": qty, "Live Share Price": f"${unit_p:.2f}", "Total Net Value": f"${tot_val:.2f}"})

    holdings_df = pd.DataFrame(holdings_data if holdings_data else [{"Asset Ticker": "NONE", "Shares Owned": 0, "Live Share Price": "$0.00", "Total Net Value": "$0.00"}])
    inventory_df = pd.DataFrame([{"Resource Class": "📦 Raw Materials ($50/unit)", "Stock Volume": f"{raw_units} Units"}, {"Resource Class": "🛠️ Factory Finished Products", "Stock Volume": f"{finished_units} Units"}])
    current_total_worth = cash + equity_value + (raw_units * prices.get("RAW_COST", 50.0))
    current_time = datetime.now().strftime("%H:%M:%S")

    history.append({"time": current_time, "worth": current_total_worth})
    if len(history) > 25: history.pop(0)

    with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
        conn.cursor().execute("UPDATE corporate_ledgers SET portfolio_value_history = ? WHERE executive = ?", (json.dumps(history), name))
        conn.commit()

    history_df = pd.DataFrame(history)
    fig = go.Figure()
    if not history_df.empty and "time" in history_df.columns:
        fig.add_trace(go.Scatter(x=history_df["time"], y=history_df["worth"], mode="lines+markers", line=dict(color="#2b6cb0", width=3.5), marker=dict(color="#3182ce", size=6)))
    fig.update_layout(paper_bgcolor="#ffffff", plot_bgcolor="#f8fafc", margin=dict(l=40, r=30, t=30, b=30))

    log_html = ""
    for r in reversed(log_rows):
        color = "#e53e3e" if r[1].upper() == "ERROR" else ("#2b6cb0" if r[1].upper() == "THOUGHT" else "#4a5568")
        log_html += f"<div><b style='color:{color};'>[{r[0]}] {r[1].upper()}:</b> {r[2].replace('\n', '<br>')}</div>"

    return f"${current_total_worth:,.2f}", holdings_df, inventory_df, log_html if log_html else "Waiting...", fig

async def handle_executive_chat(name, user_message, history):
    if not user_message: return "", history
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT cash_balance, stock_holdings FROM corporate_ledgers WHERE executive = ?", (name,))
            ledg = cursor.fetchone()
            cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
            prices = json.loads(cursor.fetchone()[0])
        context_string = f"Cash: ${ledg[0]:,.2f}, Prices: {prices}."
    except Exception:
        context_string = "Baseline active."

    personas = {
        "Warren": "You are Warren, Chief Value Officer. Conservative, prefer Apple (AAPL). Max 3 sentences.",
        "George": "You are George, Chief Macro Hedger. Tactical, hold large pure cash hoards. Max 3 sentences.",
        "Ray": "You are Ray, Chief Diversification Officer. Strict risk parity across components. Max 3 sentences.",
        "Cathie": "You are Cathie, Chief Innovation Director. Hyper-aggressive, load Tesla (TSLA). Max 3 sentences."
    }
    system_prompt = f"{personas.get(name, 'Executive AI')}\nMetrics: {context_string}"
    try:
        response = await openrouter_client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_message}],
            max_tokens=150, temperature=0.7
        )
        ai_reply = response.choices[0].message.content
    except Exception:
        ai_reply = "Secure network line active."
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": ai_reply})
    return "", history

async def run_boardroom_debate(user_prompt, history):
    if not user_prompt: return
    history.append({"role": "user", "content": f"📋 BOARDROOM PROMPT: {user_prompt}"})
    yield "", history
    for exec_name in ["George", "Warren", "Cathie", "Ray"]:
        _, single_history = await handle_executive_chat(exec_name, user_prompt, [])
        agent_response = single_history[1]["content"] if len(single_history) > 1 else "Analyzing data metrics..."
        history.append({"role": "assistant", "content": f"👔 **{exec_name}:** {agent_response}"})
        yield "", history

def trigger_market_shock_event(event_type: str):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
            prices = json.loads(cursor.fetchone()[0])
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            details = ""
            if event_type == "crash":
                prices["AAPL"] = round(prices["AAPL"] * 0.75, 2); prices["TSLA"] = round(prices["TSLA"] * 0.70, 2)
                prices["NVDA"] = round(prices["NVDA"] * 0.65, 2); prices["AMZN"] = round(prices["AMZN"] * 0.75, 2)
                details = "📉 BLACK THURSDAY: Simulated Equity Market Crash triggered (-25% Tickers)."
            elif event_type == "rally":
                prices["AAPL"] = round(prices["AAPL"] * 1.25, 2); prices["TSLA"] = round(prices["TSLA"] * 1.30, 2)
                prices["NVDA"] = round(prices["NVDA"] * 1.40, 2); prices["AMZN"] = round(prices["AMZN"] * 1.20, 2)
                details = "🚀 TECH BULL RALLY: Global liquidity influx forced sudden growth."
            elif event_type == "supply":
                prices["RAW_COST"] = round(prices["RAW_COST"] * 1.80, 2); prices["RETAIL_VALUE"] = round(prices["RETAIL_VALUE"] * 0.85, 2)
                details = "📦 SUPPLY CHAIN SHOCK: Material costs increased 80%."
            cursor.execute("UPDATE global_market_state SET value_data = ? WHERE key = 'prices'", (json.dumps(prices),))
            cursor.execute("INSERT INTO security_audit_vault (timestamp, executive, action_type, details) VALUES (?, 'SYSTEM', 'MACRO_SHOCK', ?)", (timestamp, details))
            for ex in ["Warren", "George", "Ray", "Cathie"]:
                cursor.execute("INSERT INTO system_logs (executive, timestamp, log_type, message) VALUES (?, datetime('now'), 'ERROR', ?)", (ex, details))
            conn.commit()
            return f"Success: {details}"
    except Exception as e:
        return f"Shock Controller Malfunction: {e}"

with gr.Blocks(css=premium_light_css, js=force_light_js) as app:
    with gr.Row(elem_id="master-header"):
        with gr.Column(): gr.Markdown("# 🎓 Titan Corporate Executive Network — Multi-Agent System")

    with gr.Row():
        with gr.Column(): leaderboard_plot = gr.Plot(value=fetch_global_leaderboard_chart())

    with gr.Row(elem_classes="main-dashboard-grid"):
        with gr.Column(elem_classes="dashboard-left-pane"):
            gr.Markdown("### 🌐 Live Shared Exchange Stock Tickers")
            market_table = gr.Dataframe(interactive=False)
            gr.Markdown("### 🚨 Macro System Shock Event Injector")
            with gr.Row():
                btn_crash = gr.Button("🚨 TRIGGER EQUITY MARKET CRASH (-25%)", variant="stop", elem_classes="control-btn")
                btn_rally = gr.Button("🚀 INJECT HYPER TECH BULL RALLY (+30%)", variant="primary", elem_classes="control-btn")
            btn_supply = gr.Button("📦 SIMULATE SUPPLY CHAIN CRISIS (+80% RAW COSTS)", variant="secondary", elem_classes="control-btn")
            shock_status = gr.Textbox(label="Last Executed System Shock Log Event", value="No macro override actions logged in this run window.", interactive=False)
        with gr.Column(elem_classes="dashboard-right-pane"):
            gr.Markdown("### 🔒 Secure Verification Ledger Audit Trail Checkpoints")
            vault_table = gr.Dataframe(interactive=False)

    # 👔 TAB 1: WARREN
    with gr.Tab("Warren", elem_classes="tabs"):
        with gr.Row(elem_classes="executive-row-grid"):
            with gr.Column(elem_classes="executive-left-col"):
                w_worth = gr.Textbox(label="Unified Net Asset Valuation (USD)", value="$10,000.00", interactive=False, elem_classes="stat-box")
                gr.Markdown("### 📈 Active Equity Allocations"); w_holdings = gr.Dataframe(interactive=False)
                gr.Markdown("### 🏭 Warehouse Physical Freight Stack"); w_inventory = gr.Dataframe(interactive=False)
                w_chart = gr.Plot()
            with gr.Column(elem_classes="executive-right-col"):
                gr.Markdown("### 💬 Dedicated Interview Terminal: CFO Warren")
                w_chat = gr.Chatbot(label="Secure Warren Connection Line", elem_classes="executive-chatbot-window")
                with gr.Row():
                    w_input = gr.Textbox(placeholder="Ask Executive Warren about their balance sheet...", show_label=False, scale=4)
                    w_send = gr.Button("SEND", variant="primary", scale=1)
                gr.Examples(examples=[["Warren, do you think our strategy is too safe?"], ["Warren, what is your favorite stock to buy?"]], inputs=[w_input], label="💡 Suggested strategic questions:")
        gr.Markdown("### Sat-Link Operational Activity Feed & Strategy Thoughts")
        w_console = gr.HTML(value="Initializing...", elem_classes="scroll-feed-container")

    # 👔 TAB 2: GEORGE
    with gr.Tab("George", elem_classes="tabs"):
        with gr.Row(elem_classes="executive-row-grid"):
            with gr.Column(elem_classes="executive-left-col"):
                g_worth = gr.Textbox(label="Unified Net Asset Valuation (USD)", value="$10,000.00", interactive=False, elem_classes="stat-box")
                gr.Markdown("### 📈 Active Equity Allocations"); g_holdings = gr.Dataframe(interactive=False)
                gr.Markdown("### 🏭 Warehouse Physical Freight Stack"); g_inventory = gr.Dataframe(interactive=False)
                g_chart = gr.Plot()
            with gr.Column(elem_classes="executive-right-col"):
                gr.Markdown("### 💬 Dedicated Interview Terminal: CFO George")
                g_chat = gr.Chatbot(label="Secure George Connection Line", elem_classes="executive-chatbot-window")
                with gr.Row():
                    g_input = gr.Textbox(placeholder="Ask Executive George about their balance sheet...", show_label=False, scale=4)
                    g_send = gr.Button("SEND", variant="primary", scale=1)
                gr.Examples(examples=[["George, what are you doing with our cash right now?"], ["Why shouldn't we buy stocks today, George?"]], inputs=[g_input], label="💡 Suggested strategic questions:")
        gr.Markdown("### Sat-Link Operational Activity Feed & Strategy Thoughts")
        g_console = gr.HTML(value="Initializing...", elem_classes="scroll-feed-container")

    # 👔 TAB 3: RAY
    with gr.Tab("Ray", elem_classes="tabs"):
        with gr.Row(elem_classes="executive-row-grid"):
            with gr.Column(elem_classes="executive-left-col"):
                r_worth = gr.Textbox(label="Unified Net Asset Valuation (USD)", value="$10,000.00", interactive=False, elem_classes="stat-box")
                gr.Markdown("### 📈 Active Equity Allocations"); r_holdings = gr.Dataframe(interactive=False)
                gr.Markdown("### 🏭 Warehouse Physical Freight Stack"); r_inventory = gr.Dataframe(interactive=False)
                r_chart = gr.Plot()
            with gr.Column(elem_classes="executive-right-col"):
                gr.Markdown("### 💬 Dedicated Interview Terminal: CFO Ray")
                r_chat = gr.Chatbot(label="Secure Ray Connection Line", elem_classes="executive-chatbot-window")
                with gr.Row():
                    r_input = gr.Textbox(placeholder="Ask Executive Ray about their balance sheet...", show_label=False, scale=4)
                    r_send = gr.Button("SEND", variant="primary", scale=1)
                gr.Examples(examples=[["Ray, how are you keeping our portfolio balanced?"], ["Ray, explain your mathematical risk-parity approach."]], inputs=[r_input], label="💡 Suggested strategic questions:")
        gr.Markdown("### Sat-Link Operational Activity Feed & Strategy Thoughts")
        r_console = gr.HTML(value="Initializing...", elem_classes="scroll-feed-container")

    # 👔 TAB 4: CATHIE
    with gr.Tab("Cathie", elem_classes="tabs"):
        with gr.Row(elem_classes="executive-row-grid"):
            with gr.Column(elem_classes="executive-left-col"):
                c_worth = gr.Textbox(label="Unified Net Asset Valuation (USD)", value="$10,000.00", interactive=False, elem_classes="stat-box")
                gr.Markdown("### 📈 Active Equity Allocations"); c_holdings = gr.Dataframe(interactive=False)
                gr.Markdown("### 🏭 Warehouse Physical Freight Stack"); c_inventory = gr.Dataframe(interactive=False)
                c_chart = gr.Plot()
            with gr.Column(elem_classes="executive-right-col"):
                gr.Markdown("### 💬 Dedicated Interview Terminal: CFO Cathie")
                c_chat = gr.Chatbot(label="Secure Cathie Connection Line", elem_classes="executive-chatbot-window")
                with gr.Row():
                    c_input = gr.Textbox(placeholder="Ask Executive Cathie about their balance sheet...", show_label=False, scale=4)
                    c_send = gr.Button("SEND", variant="primary", scale=1)
                gr.Examples(examples=[["Cathie, are you going to dump our capital into TSLA?"], ["Why do you run such a thin cash reserve cushion?"]], inputs=[c_input], label="💡 Suggested strategic questions:")
        gr.Markdown("### Sat-Link Operational Activity Feed & Strategy Thoughts")
        c_console = gr.HTML(value="Initializing...", elem_classes="scroll-feed-container")

    # 🏛️ TAB 5: BOARDROOM COUNCIL
    with gr.Tab("👔 Shared Boardroom Consensus Chamber", elem_classes="tabs"):
        gr.Markdown("### 🏛️ Joint Executive Council Debate Forum")
        board_chatbot = gr.Chatbot(height=450, label="Live Executive Cross-Examination Feed")
        with gr.Row():
            board_input = gr.Textbox(placeholder="Enter a strategic proposal...", show_label=False, scale=4)
            board_send = gr.Button("CONVENE COUNCIL", variant="primary", scale=1)
        gr.Examples(examples=[["Should we completely liquidate our stock holdings?"], ["Is scaling factory raw materials better than buying NVDA?"]], inputs=[board_input], label="💡 Boardroom dilemma chips:")

    w_send.click(fn=handle_executive_chat, inputs=[gr.State("Warren"), w_input, w_chat], outputs=[w_input, w_chat])
    w_input.submit(fn=handle_executive_chat, inputs=[gr.State("Warren"), w_input, w_chat], outputs=[w_input, w_chat])
    g_send.click(fn=handle_executive_chat, inputs=[gr.State("George"), g_input, g_chat], outputs=[g_input, g_chat])
    g_input.submit(fn=handle_executive_chat, inputs=[gr.State("George"), g_input, g_chat], outputs=[g_input, g_chat])
    r_send.click(fn=handle_executive_chat, inputs=[gr.State("Ray"), r_input, r_chat], outputs=[r_input, r_chat])
    r_input.submit(fn=handle_executive_chat, inputs=[gr.State("Ray"), r_input, r_chat], outputs=[r_input, r_chat])
    c_send.click(fn=handle_executive_chat, inputs=[gr.State("Cathie"), c_input, c_chat], outputs=[c_input, c_chat])
    c_input.submit(fn=handle_executive_chat, inputs=[gr.State("Cathie"), c_input, c_chat], outputs=[c_input, c_chat])
    
    board_send.click(fn=run_boardroom_debate, inputs=[board_input, board_chatbot], outputs=[board_input, board_chatbot])
    board_input.submit(fn=run_boardroom_debate, inputs=[board_input, board_chatbot], outputs=[board_input, board_chatbot])

    btn_crash.click(fn=lambda: trigger_market_shock_event("crash"), outputs=[shock_status])
    btn_rally.click(fn=lambda: trigger_market_shock_event("rally"), outputs=[shock_status])
    btn_supply.click(fn=lambda: trigger_market_shock_event("supply"), outputs=[shock_status])

    app.load(fn=lambda: fetch_executive_data("Warren"), outputs=[w_worth, w_holdings, w_inventory, w_console, w_chart])
    app.load(fn=lambda: fetch_executive_data("George"), outputs=[g_worth, g_holdings, g_inventory, g_console, g_chart])
    app.load(fn=lambda: fetch_executive_data("Ray"), outputs=[r_worth, r_holdings, r_inventory, r_console, r_chart])
    app.load(fn=lambda: fetch_executive_data("Cathie"), outputs=[c_worth, c_holdings, c_inventory, c_console, c_chart])

    global_timer = gr.Timer(value=3.0)
    global_timer.tick(fn=fetch_global_market_status, outputs=[market_table, vault_table, leaderboard_plot], show_progress="hidden", queue=False)

# 🔴 THE INTERCEPT FIX FOR RENDER CLOUD NETWORKS
if __name__ == "__main__":
    server_port = int(os.environ.get("PORT", 7860))
    print(f"🎬 Initiating full-screen light production platform on port {server_port}...")
    app.launch(
        server_name="0.0.0.0",
        server_port=server_port,
        prevent_thread_lock=True
    )