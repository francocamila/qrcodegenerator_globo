#!/usr/bin/python
import sys
from pyshorteners import Shortener
from .models import *
import requests
import shutil
import os   

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#url1 = input("Enter the URL to get QR code:")
#print(url1)
#url1= 'https://google.com'
#add ='?utm_source=tv&utm_medium=qrcode&utm_campaign=g1df'
#url = url1 + add
#shortener = Shortener('Tinyurl')
#shortener.short(url1)
#print (shortener.qrcode(300,300))

def G1(oie):
    url1= oie
    add ='?utm_source=tv&utm_medium=qrcode&utm_campaign=g1df'
    url = url1 + add
    shortener = Shortener('Tinyurl')
    shortener.short(url)
    link_image = shortener.qrcode(300,300)
    #saving
    #filename = 'qrcode1'
    #filename = link_image.split('/')[-1]
    #r = requests.get(link_image, allow_redirects=True)
    #image = r.content
    #open(filename, 'wb').write(image)
    #shutil.copy(filename, os.path.join(BASE_DIR, 'media/images'))

    return link_image

def GE(oie):
    url1= oie
    add ='?utm_source=tv&utm_medium=qrcode&utm_campaign=gedf'
    url = url1 + add
    shortener = Shortener('Tinyurl')
    shortener.short(url)
    link_image = shortener.qrcode(300,300)
    #saving
    #filename = 'qrcode1'
    #filename = link_image.split('/')[-1]
    #r = requests.get(link_image, allow_redirects=True)
    #image = r.content
    #open(filename, 'wb').write(image)
    #shutil.copy(filename, os.path.join(BASE_DIR, 'media/images'))

    return link_image








