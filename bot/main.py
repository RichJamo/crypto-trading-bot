from bot.config import API_KEY, API_SECRET
from bot.exchanges.binance_api import BinanceAPI
from bot.strategies.basic_strategy import BasicStrategy

def run_bot():
    binance = BinanceAPI(api_key=API_KEY, api_secret=API_SECRET)
    strategy = BasicStrategy(binance)
    strategy.execute()

if __name__ == "__main__":
    run_bot()
