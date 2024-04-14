import urllib.request
import smtplib, ssl
with urllib.request.urlopen('https://query1.finance.yahoo.com/v8/finance/chart/AMZN?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance/') as response:
    html = response.read()
html = str(html)
rmpindex1 = html.find("regularMarketPrice\":")
rmpindex1 = int(rmpindex1)
lengths = len("regularMarketPrice")+2
newhtml = html[rmpindex1:]
commaindex = newhtml.find(",")
marketprice = html[rmpindex1+lengths:rmpindex1+commaindex]
print("Regular Market Price: "+marketprice)


#import requests
#url = 'https://query1.finance.yahoo.com/v8/finance/chart/AMZN?region=US&lang=en-US&includePrePost=false&interval=2m&useYfid=true&range=1d&corsDomain=finance.yahoo.com&.tsrc=finance'
#r = requests.get(url)
