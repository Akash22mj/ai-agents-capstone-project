# # Updated Advanced code

# import asyncio
# import os
# import sqlite3
# import json
# import random
# import requests
# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# from agents import Agent, Runner, OpenAIChatCompletionsModel
# from agents.mcp import MCPServerStdio

# from titan_database import write_system_log, initialize_titan_db, seed_initial_corporate_state
# from titan_prompts import get_executive_prompt

# load_dotenv(override=True)
# DB_FILE = "titan_corp.db"

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# secure_key = OPENROUTER_API_KEY or "sk-or-v1-fallback-dummy-token"
# openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=secure_key)

# RUN_EVERY_N_MINUTES = 1
# MAX_TURNS = 25

# def get_free_model():
#     return OpenAIChatCompletionsModel(model="openai/gpt-oss-120b:free", openai_client=openrouter_client)

# class TitanExecutiveRunner:
#     def __init__(self, name: str):
#         self.name = name.capitalize()
#         self.model = get_free_model()
#         self.instructions = get_executive_prompt(self.name)

#     async def execute_corporate_cycle(self):
#         print(f"💼 [LOOP EXECUTION] Waking up CFO Executive: {self.name}...")
#         write_system_log(self.name, "system", "Commencing corporate state transaction optimization turn...")
#         mcp_params = {"command": "uv", "args": ["run", "titan_mcp_servers.py"]}

#         try:
#             async with MCPServerStdio(mcp_params, client_session_timeout_seconds=60) as session:
#                 agent = Agent(name=self.name, instructions=self.instructions, model=self.model, mcp_servers=[session])
#                 prompt_msg = (
#                     f"Analyze your corporate asset statement, the dynamic stock prices, and the global macro news from your tools. "
#                     f"Adjust warehouse inventory vectors, buy/sell raw materials or finished products, "
#                     f"or execute equity trades to maximize division worth. Finalize your turn decisively."
#                 )
#                 result = await Runner.run(agent, prompt_msg, max_turns=MAX_TURNS)
#                 log_output = getattr(result, "final_output", str(result))
#                 if not log_output or log_output == "None":
#                     log_output = f"[CFO {self.name}] Turn finalized. Financial allocations and supply channels audited successfully."

#                 write_system_log(self.name, "thought", log_output)
#                 print(f"✅ [SUCCESS] CFO {self.name} finalized their strategy execution run safely.")
#         except Exception as e:
#             print(f"❌ [LOOP ERROR] {self.name}: {e}")
#             write_system_log(self.name, "error", f"Exception hit: {e}")

# async def macro_broker_event_loop():
#     """🌐 NEW 200% ENGINE LAYER: Simulates dynamic random world-wide economic shocks and adjusts item values."""
#     news_events = [
#         ("🚨 RAW MATERIAL EXPLOSION: Supply chain panic! Raw components cost spikes to $110/unit.", {"RAW_COST": 110.0, "RETAIL_VALUE": 430.0}),
#         ("📈 TECH DEVICE BOOM: Consumer product demand surges! Finished goods selling price increases to $580/cash profit unit.", {"RAW_COST": 55.0, "RETAIL_VALUE": 580.0}),
#         ("📉 COMMODITY REBOUND: Global cargo freight lanes drop values. Raw components drop to discount price of $35/unit.", {"RAW_COST": 35.0, "RETAIL_VALUE": 380.0}),
#         ("🛡️ STABLE GROWTH PATTERN: Federal interest rates drop. Corporate stock allocations receive macro tailwinds.", {"RAW_COST": 50.0, "RETAIL_VALUE": 400.0})
#     ]
    
#     while True:
#         await asyncio.sleep(120) # Inject a brand new global economic crisis/boom every 2 minutes!
#         selected_news, price_adjustments = random.choice(news_events)
#         print(f"📡 [MACRO BROKER EVENT] -> {selected_news}")
        
#         try:
#             with sqlite3.connect(DB_FILE, timeout=30.0) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT value_data FROM global_market_state WHERE key = 'prices'")
#                 current_prices = json.loads(cursor.fetchone()[0])
                
#                 # Merge macro changes back into active stock exchange ticker arrays
#                 current_prices.update(price_adjustments)
                
#                 cursor.execute("UPDATE global_market_state SET value_data = ? WHERE key = 'prices'", (json.dumps(current_prices),))
#                 cursor.execute("UPDATE global_market_state SET value_data = ? WHERE key = 'macro_news'", (selected_news,))
#                 conn.commit()
                
#             for name in ["Warren", "George", "Ray", "Cathie"]:
#                 write_system_log(name, "system", f"🌐 GLOBAL MARKET BROKER SIGNAL: {selected_news}")
#         except Exception as e:
#             print(f"⚠️ Macro broker exception: {e}")

# async def main_automation_loop():
#     print("🚀 [CORE BOOT] Initializing 200% Advanced Capstone Processing Thread Network...")
#     executives = ["Warren", "George", "Ray", "Cathie"]
#     runners = [TitanExecutiveRunner(name) for name in executives]

#     # Spawn macro event engine concurrently right next to our agents!
#     asyncio.create_task(macro_broker_event_loop())

#     print("⚡ [CORE LOOP ACTIVE] Entering automated evaluation cycles structure.")
#     while True:
#         for runner in runners:
#             await runner.execute_corporate_cycle()
#             await asyncio.sleep(4)
#         print(f"💤 Loop cycle complete. Sleeping for {RUN_EVERY_N_MINUTES} minute(s)...")
#         await asyncio.sleep(RUN_EVERY_N_MINUTES * 60)

# if __name__ == "__main__":
#     print("🎬 Framework entry execution trigger initialized.")
#     initialize_titan_db()
#     seed_initial_corporate_state()
    
#     user_key = os.getenv("PUSHOVER_USER")
#     token_key = os.getenv("PUSHOVER_TOKEN")
#     if user_key and token_key:
#         try:
#             requests.post("https://api.pushover.net/1/messages.json", data={"user": user_key, "token": token_key, "message": "🎓 Capstone Network: 200% Advanced Market Broker Engine Online!"}, timeout=5)
#         except Exception: pass

#     asyncio.run(main_automation_loop())


# Central Advanced code

# import asyncio
# import os
# import sqlite3
# import json
# import requests
# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# from agents import Agent, Runner, OpenAIChatCompletionsModel
# from agents.mcp import MCPServerStdio

# from titan_database import write_system_log, initialize_titan_db, seed_initial_corporate_state
# from titan_prompts import get_executive_prompt

# # load_dotenv(override=True)
# # Force absolute path resolution for the local folder .env file
# from pathlib import Path
# current_dir = Path(__file__).parent.resolve()
# load_dotenv(dotenv_path=current_dir / ".env", override=True)
# DB_FILE = "titan_corp.db"

# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# secure_key = OPENROUTER_API_KEY or "sk-or-v1-fallback-dummy-token"
# openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=secure_key)

# RUN_EVERY_N_MINUTES = 1
# MAX_TURNS = 25

# def get_free_model():
#     return OpenAIChatCompletionsModel(model="openai/gpt-oss-120b:free", openai_client=openrouter_client)

# class TitanExecutiveRunner:
#     def __init__(self, name: str):
#         self.name = name.capitalize()
#         self.model = get_free_model()
#         self.instructions = get_executive_prompt(self.name)

#     async def execute_corporate_cycle(self):
#         print(f"💼 [LOOP EXECUTION] Waking up CFO Executive: {self.name}...")
#         write_system_log(self.name, "system", "Commencing corporate state transaction optimization turn...")
#         mcp_params = {"command": "uv", "args": ["run", "titan_mcp_servers.py"]}

#         try:
#             async with MCPServerStdio(mcp_params, client_session_timeout_seconds=60) as session:
#                 agent = Agent(name=self.name, instructions=self.instructions, model=self.model, mcp_servers=[session])
#                 prompt_msg = (
#                     f"Analyze your corporate asset statement, live ticker prices, and rival inventory counts from your tools. "
#                     f"Optimize your balance sheet: manage your supply chain lines, buy/sell stock assets, or execute direct "
#                     f"inter-agent B2B contract trades with competitor rivals if mutually profitable. Conclude your turn decisively."
#                 )
#                 result = await Runner.run(agent, prompt_msg, max_turns=MAX_TURNS)
#                 log_output = getattr(result, "final_output", str(result))
#                 if not log_output or log_output == "None":
#                     log_output = f"[CFO {self.name}] Turn finalized safely. Asset profiles updated over local data bridges."

#                 write_system_log(self.name, "thought", log_output)
#                 print(f"✅ [SUCCESS] CFO {self.name} finalized their strategy execution run safely.")
#         except Exception as e:
#             print(f"❌ [LOOP ERROR] {self.name}: {e}")
#             write_system_log(self.name, "error", f"Exception hit: {e}")

# async def main_automation_loop():
#     print("🚀 [CORE BOOT] Initializing Clean & Advanced B2B Agent Network Core...")
#     initialize_titan_db()
#     seed_initial_corporate_state()

#     executives = ["Warren", "George", "Ray", "Cathie"]
#     runners = [TitanExecutiveRunner(name) for name in executives]

#     print("⚡ [CORE LOOP ACTIVE] Entering evaluation tree sequence loops.")
#     while True:
#         for runner in runners:
#             await runner.execute_corporate_cycle()
#             await asyncio.sleep(4)
#         print(f"💤 Loop execution segment complete. Sleeping for {RUN_EVERY_N_MINUTES} minute(s)...")
#         await asyncio.sleep(RUN_EVERY_N_MINUTES * 60)

# if __name__ == "__main__":
#     print("🎬 Framework entry execution trigger initialized.")
#     asyncio.run(main_automation_loop())


# updated error code

import asyncio
import os
import sqlite3
import json
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
from agents.mcp import MCPServerStdio

from titan_database import write_system_log, initialize_titan_db, seed_initial_corporate_state
from titan_prompts import get_executive_prompt

DB_FILE = "titan_corp.db"
RUN_EVERY_N_MINUTES = 1
MAX_TURNS = 25

# Clean direct text extraction from your local folder file
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

# Clear out standard OpenAI environment channel to prevent framework confusion
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

os.environ["OPENROUTER_API_KEY"] = direct_token

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=direct_token)

def get_free_model():
    return OpenAIChatCompletionsModel(model="openai/gpt-oss-120b:free", openai_client=openrouter_client)

# def get_free_model():
#     return OpenAIChatCompletionsModel(model="openai/gpt-oss-20b:free", openai_client=openrouter_client)

class TitanExecutiveRunner:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.model = get_free_model()
        self.instructions = get_executive_prompt(self.name)

    async def execute_corporate_cycle(self):
        print(f"💼 [LOOP EXECUTION] Waking up CFO Executive: {self.name}...")
        write_system_log(self.name, "system", "Commencing corporate state transaction optimization turn...")
        mcp_params = {"command": "uv", "args": ["run", "titan_mcp_servers.py"]}

        try:
            async with MCPServerStdio(mcp_params, client_session_timeout_seconds=60) as session:
                agent = Agent(name=self.name, instructions=self.instructions, model=self.model, mcp_servers=[session])
                prompt_msg = (
                    f"Analyze your corporate asset statement, live ticker prices, and rival inventory counts from your tools. "
                    f"Optimize your balance sheet: manage your supply chain lines, buy/sell stock assets, or execute direct "
                    f"inter-agent B2B contract trades with competitor rivals if mutually profitable. Conclude your turn decisively."
                )
                result = await Runner.run(agent, prompt_msg, max_turns=MAX_TURNS)
                log_output = getattr(result, "final_output", str(result))
                if not log_output or log_output == "None":
                    log_output = f"[CFO {self.name}] Turn finalized safely. Asset profiles updated over local data bridges."

                write_system_log(self.name, "thought", log_output)
                print(f"✅ [SUCCESS] CFO {self.name} finalized their strategy execution run safely.")
        except Exception as e:
            print(f"❌ [LOOP ERROR] {self.name}: {e}")
            write_system_log(self.name, "error", f"Exception hit: {e}")

async def main_automation_loop():
    print("🚀 [CORE BOOT] Initializing Clean & Advanced B2B Agent Network Core...")
    initialize_titan_db()
    seed_initial_corporate_state()

    executives = ["Warren", "George", "Ray", "Cathie"]
    runners = [TitanExecutiveRunner(name) for name in executives]

    print("⚡ [CORE LOOP ACTIVE] Entering evaluation tree sequence loops.")
    while True:
        for runner in runners:
            await runner.execute_corporate_cycle()
            await asyncio.sleep(4)
        print(f"💤 Loop execution segment complete. Sleeping for {RUN_EVERY_N_MINUTES} minute(s)...")
        await asyncio.sleep(RUN_EVERY_N_MINUTES * 60)

if __name__ == "__main__":
    print("🎬 Framework entry execution trigger initialized.")
    asyncio.run(main_automation_loop())