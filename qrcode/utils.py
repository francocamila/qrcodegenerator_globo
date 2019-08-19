#!/usr/bin/python
from pyshorteners import Shortener

#url1 = input("Enter the URL to get QR code:")
#print(url1)
#url1= 'https://google.com'
#add ='?utm_source=tv&utm_medium=qrcode&utm_campaign=g1df'
#url = url1 + add
#shortener = Shortener('Tinyurl')
#shortener.short(url1)
#print (shortener.qrcode(300,300))

def oi():
    url1= 'https://google.com'
    add ='?utm_source=tv&utm_medium=qrcode&utm_campaign=g1df'
    url = url1 + add
    shortener = Shortener('Tinyurl')
    shortener.short(url1)
    return shortener.qrcode(300,300)
