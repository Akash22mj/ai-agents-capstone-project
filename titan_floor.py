# # updated error code

# import asyncio
# import os
# import sqlite3
# import json
# from openai import AsyncOpenAI
# from agents import Agent, Runner, OpenAIChatCompletionsModel
# from agents.mcp import MCPServerStdio

# from titan_database import write_system_log, initialize_titan_db, seed_initial_corporate_state
# from titan_prompts import get_executive_prompt

# DB_FILE = "titan_corp.db"
# RUN_EVERY_N_MINUTES = 1
# MAX_TURNS = 25

# # Clean direct text extraction from your local folder file
# def load_key_directly():
#     try:
#         with open(".env", "r") as f:
#             for line in f:
#                 if "OPENROUTER_API_KEY" in line:
#                     return line.split("=")[1].strip().strip('"').strip("'")
#     except Exception:
#         pass
#     return "sk-or-v1-fallback-dummy-token"

# direct_token = load_key_directly()

# # Clear out standard OpenAI environment channel to prevent framework confusion
# if "OPENAI_API_KEY" in os.environ:
#     del os.environ["OPENAI_API_KEY"]

# os.environ["OPENROUTER_API_KEY"] = direct_token

# OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=direct_token)

# def get_free_model():
#     return OpenAIChatCompletionsModel(model="openai/gpt-oss-120b:free", openai_client=openrouter_client)

# # def get_free_model():
# #     return OpenAIChatCompletionsModel(model="openai/gpt-oss-20b:free", openai_client=openrouter_client)

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

# Github code next

import asyncio
import os
import sqlite3
import json
import sys
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
from agents.mcp import MCPServerStdio

from titan_database import write_system_log, initialize_titan_db, seed_initial_corporate_state
from titan_prompts import get_executive_prompt

DB_FILE = "titan_corp.db"
RUN_EVERY_N_MINUTES = 1
MAX_TURNS = 25

# 🔴 FIX: First try pulling directly from Render Cloud Variables, then fallback to local file if running at home
direct_token = os.getenv("OPENROUTER_API_KEY")

if not direct_token:
    try:
        with open(".env", "r") as f:
            for line in f:
                if "OPENROUTER_API_KEY" in line:
                    direct_token = line.split("=")[1].strip().strip('"').strip("'")
    except Exception:
        pass

if not direct_token:
    direct_token = "sk-or-v1-fallback-dummy-token"

# Clear out standard OpenAI environment channel to prevent framework confusion
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

os.environ["OPENROUTER_API_KEY"] = direct_token

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter_client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=direct_token)

def get_free_model():
    return OpenAIChatCompletionsModel(model="openai/gpt-oss-120b:free", openai_client=openrouter_client)

class TitanExecutiveRunner:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.model = get_free_model()
        self.instructions = get_executive_prompt(self.name)

    async def execute_corporate_cycle(self):
        print(f"💼 [LOOP EXECUTION] Waking up CFO Executive: {self.name}...")
        write_system_log(self.name, "system", "Commencing corporate state transaction optimization turn...")
        
        # 🔴 FIX: Changed command from 'uv run' to native 'sys.executable' (python3) for clean cloud pipe support
        mcp_params = {"command": sys.executable, "args": ["titan_mcp_servers.py"]}

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