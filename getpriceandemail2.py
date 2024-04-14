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


# to run local email run below
# projectprice python -m smtpd -c DebuggingServer -n localhost:1025


# email
#port  = 1025
#password = input("Type your password and press enter: ")

# Create a secure SSL context
#context = ssl.create_default_context()

#with smtplib.SMTP_SSL("localhost", port, context = context) as server:
#    server.login("shriyaalovesdolphins@gmail.com", password)
    # TODO: Send email here

tolist=["one@one.org","two@two.org"]  
msg = "Hi Shriyaa \r\n \r\n Regular Market Price: "+marketprice  
 #... From: Me@my.org  
 #... Subject: testin'... 3


s=smtplib.SMTP("localhost:1025")  
s.sendmail("me@my.org",tolist,msg)
s.quit() 