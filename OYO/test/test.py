import re
import csv
import time
import math
import json
import requests
import numpy as np
import pandas as pd
import urllib.request
from compute import compute_dlf, compute_cyber, compute_huda, Merge

from bs4 import BeautifulSoup
    
url_list = ['https://www.oyorooms.com/search?country=India&filters%5Bcoordinates%5D%5Blatitude%5D=28.45911&filters%5Bcoordinates%5D%5Blongitude%5D=77.07255&filters%5Broom_pricing%5D%5Bmax%5D=3632&filters%5Broom_pricing%5D%5Bmin%5D=2120&latitude=28.45911&location=Huda+City+Center+Metro&longitude=77.07255&searchType=locality',
            'https://www.oyorooms.com/search?checkin=13%2F08%2F2019&checkout=14%2F08%2F2019&city=undefined&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.4949762&filters%5Bcoordinates%5D%5Blongitude%5D=77.0895421&filters%5Broom_pricing%5D%5Bmax%5D=5157&filters%5Broom_pricing%5D%5Bmin%5D=1617&guests=1&latitude=28.4949762&location=Dlf+Cyber+City%2C+Gurugram%2C+Haryana&longitude=77.0895421&roomConfig%5B%5D=1&rooms=1&searchType=locality&showSearchElements=false',
            'https://www.oyorooms.com/search?checkin=13%2F08%2F2019&checkout=14%2F08%2F2019&city=undefined&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.471981&filters%5Bcoordinates%5D%5Blongitude%5D=77.104735&filters%5Broom_pricing%5D%5Bmax%5D=4020&filters%5Broom_pricing%5D%5Bmin%5D=2169&guests=2&latitude=28.471981&location=DLF+Phase+1%2C+Gurgaon%2C+Haryana&longitude=77.104735&roomConfig%5B%5D=2&rooms=1&searchType=locality&showSearchElements=false'
           ]

filename = 'hotel.csv'
combined_list = []
dlf_data_dict = {}
cyber_data_dict = {}
huda_data_dict = {}
dict3 = {}
dict4 = {}
column_header = ['Name', 'Price', 'Region', 'Date']

with open(filename, 'w') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(column_header)
write_file.close()

for url in url_list:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    names = [a.get_text() for a in soup.find_all('h3', {"class": "listingHotelDescription__hotelName d-textEllipsis"})]
    price = [a.get_text() for a in soup.find_all('span', {"class": "listingPrice__finalPrice"})]
    region = [a.get_text() for a in soup.find_all('h1', {"class": "ListingContentHeader__h1"})]
    date = [a.get_text() for a in soup.find_all('span', {"class": "headerDatePicker__date u-textEllipsis"})]

    with open(filename, 'a') as write_file:
        writer = csv.writer(write_file)
        
        for a, b in zip(names, price):
            combined_list.append(a)
            b = b[1:]
            combined_list.append(b)
            combined_list.append(region[0])
            combined_list.append(date[0])
            writer.writerow(combined_list)
            combined_list = []
    write_file.close()

df = pd.read_csv(filename)

for i in df.index:

    location = str(df['Region'][i])

    found_dlf = location.find('DLFPhase1')
    found_cyber = location.find('CyberCity')
    found_huda = location.find('HudaCity')
    

    if found_dlf != -1:

        data = df['Region']==location
        dlf_data = df[data]

    elif found_cyber != -1:

        data = df['Region']==location
        cyber_data = df[data]


    elif found_huda != -1:

        data = df['Region']==location
        huda_data = df[data]

    else:
        pass

dlf_data_dict = compute_dlf(dlf_data)
cyber_data_dict = compute_cyber(cyber_data)
huda_data_dict = compute_huda(huda_data)





