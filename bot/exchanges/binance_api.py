import ccxt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class BinanceAPI:
    def __init__(self, api_key=None, api_secret=None):
        """
        Initializes the BinanceAPI class with provided API key and secret.
        Uses environment variables if no keys are passed in.
        """
        self.api_key = api_key or os.getenv('API_KEY')
        self.api_secret = api_secret or os.getenv('SECRET_KEY')

        if not self.api_key or not self.api_secret:
            raise ValueError("API Key and Secret Key must be provided or set in the environment.")

        # Initialize the ccxt Binance client
        self.client = ccxt.binance({
            'apiKey': self.api_key,
            'secret': self.api_secret,
        })

    def fetch_balance(self):
        """
        Fetches the account balance from Binance.
        """
        try:
            balance = self.client.fetch_balance()
            return balance
        except Exception as e:
            print(f"Error fetching balance: {e}")
            return None

    def place_order(self, symbol, side, order_type, amount, price=None):
        """
        Places an order on the Binance exchange.
        
        Parameters:
        - symbol: Trading pair (e.g., 'BTC/USDT')
        - side: 'buy' or 'sell'
        - order_type: 'market' or 'limit'
        - amount: The amount of the asset to trade
        - price: The price (for limit orders)
        """
        try:
            if order_type == 'limit':
                order = self.client.create_limit_order(symbol, side, amount, price)
            elif order_type == 'market':
                order = self.client.create_market_order(symbol, side, amount)
            else:
                raise ValueError("Order type must be 'limit' or 'market'")
            return order
        except Exception as e:
            print(f"Error placing order: {e}")
            return None

    def fetch_ticker(self, symbol):
        """
        Fetches the latest ticker information for a specific trading pair.
        
        Parameters:
        - symbol: Trading pair (e.g., 'BTC/USDT')
        """
        try:
            ticker = self.client.fetch_ticker(symbol)
            return ticker
        except Exception as e:
            print(f"Error fetching ticker: {e}")
            return None
