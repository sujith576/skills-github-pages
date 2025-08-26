import asyncio
import logging
import os
import sys
from dotenv import load_dotenv
from browser_use_agent.agent import Agent
from browser_use_agent.llm import ChatOpenAI

load_dotenv()

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

api_key= os.getenv("OPENAI_API_KEY")
print("API key loaded:",bool(api_key))

async def main():
    task = """
    1. Open Zepto website.
    2. Log in with my saved credentials (phone/email + password).
    3. Search for 'yogurt'.
    4. Add the first available yogurt to cart.
    5. Proceed to checkout, but stop before payment.
    """
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="o4-mini", temperature=0.7),
    )
    try:
        await agent.run()
    except Exception as e:
        logging.error("Agent execution failed: %s", e)

if __name__ == "__main__":
    asyncio.run(main())