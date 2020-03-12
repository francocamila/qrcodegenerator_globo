#!/usr/bin/python
import sys
from pyshorteners import Shortener
from .models import *
import requests
import shutil
import os 
from djqscsv import render_to_csv_response
from djqscsv import write_csv
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def qr_generator(original_url, add):

    url = original_url + add
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



def G1(original_url):
    link_image = qr_generator(original_url, add)
    post = Post()
    post.url = original_url
    post.category = 'G1'
    post.save()
    return link_image

def GE(original_url):
    link_image = qr_generator(original_url, add)
    post = Post()
    post.url = original_url
    post.category = 'GE'
    post.save()
    return link_image







