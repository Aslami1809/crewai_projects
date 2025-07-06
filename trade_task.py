from crewai import Task
from agents.trader_agent import trader_agent

stock_data = "Current stock price: $175.23, Daily price change and percentage: +2.15 (1.23%), Volume and volatility: Trading volume is 82,145,000 shares"

trade_decision = Task(
    description=(
        f"Based on the following stock data: {stock_data}, recommend whether to **Buy**, **Sell**, or **Hold** the stock."
    ),
    expected_output=(
        "A clear and confident trading recommendation (Buy / Sell / Hold), supported by a justification for the trading action."
    ),
    agent=trader_agent
)
