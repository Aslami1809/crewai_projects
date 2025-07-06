from os import environ
from crewai import Agent, LLM
from tools.stock_research_tool import get_stock_price

environ['GROQ_API_KEY'] = 'YOUR_API_KEY'

llm = LLM(
    model="deepseek-r1-distill-llama-70b",
    temperature=0
)

trader_agent = Agent(
    role="Strategic Stock Trader",
    goal = (
        "Decide whether to Buy, Sell, or Hold a given stock based on live market data, "
        "price movements, and financial analysis with the available data."
    ),
    backstory = (
        "You are a strategic trader with years of experience in timing market entry and exit points. "
        "You rely on real-time stock data, daily price movements, and volume trends to make trading decisions "
        "that optimize returns and reduce risk."
    ),
    llm=llm,
    tools=[get_stock_price],
    verbose=True

)
