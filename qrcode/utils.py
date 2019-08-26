#!/usr/bin/python
import sys
from pyshorteners import Shortener
import requests

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
    shortener.short(url)
    link_image = shortener.qrcode(300,300)
    #saving
    filename = link_image.split('/')[-1]
    r = requests.get(link_image, allow_redirects=True)
    image = r.content
    return image









