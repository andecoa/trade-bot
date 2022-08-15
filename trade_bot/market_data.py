import requests
import time

def getMarketData(symbol: str):
    """Returns the price for a given symbol"""
    x = requests.get(
        "https://finnhub.io/api/v1/quote",
        params={"symbol": symbol, "token": "cbsjggaad3i9sd7nbvp0"},
    )

    return float(x.text.split(",")[0][5:])

while True:
    print(getMarketData("GME"))
    time.sleep(60)
