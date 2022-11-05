import requests
import json

loop = 1

session = requests.session()
def GetBTC(addrU):
    request = session.get(f'http://127.0.0.1:5000/balance?active=' + addrU)
    request = request.text
    balance1 = request
    return balance1

if loop == 1:
    while True:
        r = GetBTC("1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF")
        print(f"Balance: {r}")
else:
    r = GetBTC("1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF")
    print(f"Balance: {r}")
