import os
from dotenv import load_dotenv

os.environ['GROQ_API_KEY'] = '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'

from crew import stock_crew

load_dotenv()

def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    print(result)

if __name__ == "__main__":
    run("APPLE")
    # run("APPLE")  # Uncomment to test with Apple stock
    # run("GOOGL")  # Uncomment to test with Google stock
