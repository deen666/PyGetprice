import requests
def getprice(a):
    coins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=100000000000").json()
    sms = []
    for items in coins:
		if items["symbol"] == a:
			x = "" + items['symbol'] + ': '+'$ '+ items['price_usd']+" ("+items['percent_change_24h']+"%)"
			print(x)
getprice("BTC")
