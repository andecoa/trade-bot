from sanic import Sanic
from sanic.response import text, json

app = Sanic("TradeBot")


@app.get("/trade")
async def trade(request):
    return text("Trade Bot")


if __name__ == "__main__":
    app.run(dev=True)
