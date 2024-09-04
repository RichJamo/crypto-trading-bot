import unittest
from bot.exchanges.binance_api import BinanceAPI

class TestBot(unittest.TestCase):
    def test_fetch_balance(self):
        binance = BinanceAPI(api_key="test_key", api_secret="test_secret")
        balance = binance.fetch_balance()
        self.assertIsNotNone(balance)

if __name__ == "__main__":
    unittest.main()
