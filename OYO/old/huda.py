import re
import csv
import time
import math
import requests
import numpy as np
import pandas as pd
import urllib.request

from bs4 import BeautifulSoup

def scrap_huda(all_data = {}):
    
    url_list = ['https://www.oyorooms.com/search?checkin=06%2F08%2F2019&checkout=07%2F08%2F2019&city=undefined&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.45911&filters%5Bcoordinates%5D%5Blongitude%5D=77.07255&filters%5Broom_pricing%5D%5Bmax%5D=3036&filters%5Broom_pricing%5D%5Bmin%5D=2168&guests=1&latitude=28.45911&location=Huda+City+Center+Metro%2C+Gurugram%2C+Haryana&longitude=77.07255&roomConfig%5B%5D=1&rooms=1&searchType=locality&showSearchElements=false']
    
    filename = 'huda_hotel.csv'
    name_list = []  
    price_list = []
    combined_list = []
    data_dict = {}

    for url in url_list:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        names = soup.find_all('h3', {"class": "listingHotelDescription__hotelName d-textEllipsis"})
        price = soup.find_all('span', {"class": "listingPrice__finalPrice"})

        count = -1

        for i in names:

            name_string_final = ''

            name_string = str(i)
            x = re.search(">", name_string)
            start_index = x.start()

            for j in name_string:

                count += 1
            
                if count > start_index:

                    if j == '<':
                        break

                    else:               
                        name_string_final += j

            count = -1
            name_list.append(name_string_final)

        for i in price:

            price_string_final = ''

            price_string = str(i)
            z = re.search(">", price_string)
            start_price_index = z.start()

            for j in price_string:

                count += 1
            
                if count > start_price_index+1:

                    if j == '<':
                        break

                    else:               
                        price_string_final += j

            count = -1
            price_list.append(price_string_final)

    column_header = ['Name', 'Price']

    with open(filename, 'w') as write_file:

        writer = csv.writer(write_file)
        writer.writerow(column_header)

        for i in name_list:
            for j in price_list:

                name = i
                price = j
                combined_list.append(i)
                combined_list.append(j)

                writer.writerow(combined_list)
                combined_list = []

    df = pd.read_csv(filename)

    avg_price = df['Price'].mean()
    max_price = df['Price'].max()
    min_price = df['Price'].min()
    median_price = df['Price'].median()
    std_dev = df['Price'].std()
    # variance = df['Price'].var()
    tenth_percentile = np.percentile(df['Price'], [10])
    nintyth_percentile = np.percentile(df['Price'], [90])

    data_dict['avg_price'] = math.floor(avg_price)
    data_dict['max_price'] = math.floor(max_price)
    data_dict['min_price'] = math.floor(min_price)
    data_dict['median_price'] = math.floor(median_price)
    data_dict['std_dev'] = math.floor(std_dev)
    # data_dict['variance'] = math.floor(variance)
    data_dict['tenth_percentile'] = math.floor(tenth_percentile)
    data_dict['nineth_percentile'] = math.floor(nintyth_percentile)

    return data_dict
