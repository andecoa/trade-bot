import finnhub
import time
import os


class MarketData:
    key = os.environ["API_KEY"]

    def __init__(self):
        self.finnhub_client = finnhub.Client(api_key=MarketData.key)

    def quote(self, symbol: str):
        """Returns the price for a given symbol"""
        return self.finnhub_client.quote(symbol)["c"]


"""
md = MarketData()

while True:
    print(md.quote("BINANCE:BTCUSDT"))
    time.sleep(60)
"""
