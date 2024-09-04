from bot.exchanges.binance_api import BinanceAPI
from bot.config import API_KEY, SECRET_KEY

def run_bot():
    # Initialize the Binance API client
    binance = BinanceAPI(api_key=API_KEY, api_secret=SECRET_KEY)

    # Fetch and print account balance
    balance = binance.fetch_balance()
    print("Balance:", balance)

    # Fetch and print the ticker for BTC/USDT
    ticker = binance.fetch_ticker('BTC/USDT')
    print("BTC/USDT Ticker:", ticker)

    # Example of placing a market buy order for 0.001 BTC
    # order = binance.place_order('BTC/USDT', 'buy', 'market', 0.001)
    # print("Order Result:", order)

if __name__ == "__main__":
    run_bot()
