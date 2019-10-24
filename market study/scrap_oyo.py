import re
import csv
import time
import math
import json
import requests
import numpy as np
import pandas as pd
import urllib.request

from bs4 import BeautifulSoup
from compute_dlf import compute_dlf_avg, compute_dlf_index, compute_dlf_median, compute_dlf_nine_percentile, compute_dlf_ten_percentile, compute_dlf_std
from compute_cyber import compute_cyber_avg, compute_cyber_median, compute_cyber_index, compute_cyber_nine_percentile, compute_cyber_std, compute_cyber_ten_percentile
from compute_huda import compute_huda_avg, compute_huda_median, compute_huda_index, compute_huda_nine_percentile, compute_huda_std, compute_huda_ten_percentile


data_dict = {}
data_dict["dlf_phase_1"] = {}
data_dict["dlf_cyber_city"] = {}
data_dict["huda_city_center"] = {}

#phase1 = 1700-2000 => 2800-3000 => 2800-3200 => range(26-3700)
#cc = 1800-2500 => 2000-2400 => range(1900- 2500)
#huda = 2000-3000 => 2700-3000 => range(26-3800)

def scrap_oyo(all_data = {}):

    url_list = ['https://www.oyorooms.com/search?checkin=24%2F10%2F2019&checkout=25%2F10%2F2019&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.471981&filters%5Bcoordinates%5D%5Blongitude%5D=77.104735&filters%5Broom_pricing%5D%5Bmax%5D=3718&filters%5Broom_pricing%5D%5Bmin%5D=2526&guests=1&latitude=28.471981&location=DLF+Phase+1%2C+Gurgaon%2C+Haryana&longitude=77.104735&roomConfig%5B%5D=1&rooms=1&searchType=locality',
                'https://www.oyorooms.com/search?checkin=24%2F10%2F2019&checkout=25%2F10%2F2019&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.4949762&filters%5Bcoordinates%5D%5Blongitude%5D=77.0895421&filters%5Broom_pricing%5D%5Bmax%5D=2506&filters%5Broom_pricing%5D%5Bmin%5D=1890&guests=1&latitude=28.4949762&location=Dlf+Cyber+City%2C+Gurugram%2C+Haryana&longitude=77.0895421&roomConfig%5B%5D=1&rooms=1&searchType=locality',
                'https://www.oyorooms.com/search?checkin=24%2F10%2F2019&checkout=25%2F10%2F2019&filters%5Bcoordinates%5D%5Blatitude%5D=28.4592693&filters%5Bcoordinates%5D%5Blongitude%5D=77.07241920000001&filters%5Broom_pricing%5D%5Bmax%5D=3817&filters%5Broom_pricing%5D%5Bmin%5D=2486&guests=1&latitude=28.4592693&location=Huda+Metro+Station%2C+Gurugram%2C+Delhi+122007&longitude=77.07241920000001&roomConfig%5B%5D=1&rooms=1&searchType=locality'
                ]

    combined_list = []
    filename = 'hotel.csv'  
    # column_header = ['Name', 'Price', 'Region', 'Date', 'min_price', 'max_price'] 

    # with open(filename, 'w') as write_file:
    #     writer = csv.writer(write_file)
    #     writer.writerow(column_header)
    # write_file.close()

    for url in url_list:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        names = [a.get_text() for a in soup.find_all('h3', {"class": "listingHotelDescription__hotelName d-textEllipsis"})]
        price = [a.get_text() for a in soup.find_all('span', {"class": "listingPrice__finalPrice"})]
        region = [a.get_text() for a in soup.find_all('h1', {"class": "ListingContentHeader__h1"})]
        date = [a.get_text() for a in soup.find_all('span', {"class": "headerDatePicker__date u-textEllipsis"})]
        price_range = [a.get_text() for a in soup.find_all('span', {"class": "input-range__label-container"})]

        with open(filename, 'a') as write_file:

            writer = csv.writer(write_file)
            
            for a, b in zip(names, price):

                combined_list.append(a)
                b = b[1:]
                combined_list.append(b)
                combined_list.append(region[0])
                combined_list.append(date[0])
                combined_list.append(price_range[1])
                combined_list.append(price_range[2])

                writer.writerow(combined_list)
                combined_list = []

        write_file.close()

    df = pd.read_csv(filename)

    for i in df.index:

        location = str(df['Region'][i])

        found_dlf = location.find('Phase')
        found_cyber = location.find('Cyber')
        found_huda = location.find('Huda')


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
    
    # print(dlf_data)
    # print(cyber_data)
    # print(huda_data)

    data_dict["dlf_phase_1"]["avg_price"] = compute_dlf_avg(dlf_data)
    dlf_median = compute_dlf_median(dlf_data)
    data_dict["dlf_phase_1"]["median_price"] = dlf_median
    data_dict["dlf_phase_1"]["std_deviation"] = compute_dlf_std(dlf_data)
    data_dict["dlf_phase_1"]["tenth_percentile"] = compute_dlf_ten_percentile(dlf_data)
    data_dict["dlf_phase_1"]["nineth_percentile"] = compute_dlf_nine_percentile(dlf_data)
    data_dict["dlf_phase_1"]["price_index"] = compute_dlf_index(dlf_median)

    data_dict["dlf_cyber_city"]["avg_price"] = compute_cyber_avg(cyber_data)
    cyber_median = compute_cyber_median(cyber_data)
    data_dict["dlf_cyber_city"]["median_price"] = cyber_median
    data_dict["dlf_cyber_city"]["std_deviation"] = compute_cyber_std(cyber_data)
    data_dict["dlf_cyber_city"]["tenth_percentile"] = compute_cyber_ten_percentile(cyber_data)
    data_dict["dlf_cyber_city"]["nineth_percentile"] = compute_cyber_nine_percentile(cyber_data)
    data_dict["dlf_cyber_city"]["price_index"] = compute_cyber_index(cyber_median)

    data_dict["huda_city_center"]["avg_price"] = compute_huda_avg(huda_data)
    huda_median = compute_huda_median(huda_data)
    data_dict["huda_city_center"]["median_price"] = huda_median
    data_dict["huda_city_center"]["std_deviation"] = compute_huda_std(huda_data)
    data_dict["huda_city_center"]["tenth_percentile"] = compute_huda_ten_percentile(huda_data)
    data_dict["huda_city_center"]["nineth_percentile"] = compute_huda_nine_percentile(huda_data)
    data_dict["huda_city_center"]["price_index"] = compute_huda_index(huda_median)

    return data_dict
