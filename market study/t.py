# import requests
# import json
# import datetime

# # receive_here = "https://api.nodal.direct/v1/index.php/Api/getGroupDynamicPrice"
# # received_data = requests.get(url = receive_here)
# # api_data = received_data.json()

# # print(api_data)

# import urllib.parse as urlparse
# from urllib.parse import urlencode

# url = "https://api.nodal.direct/v1/index.php/Api/getDynamicPriceWithDate?date=2019-08-26"

# prev_date_param = datetime.date.today()-datetime.timedelta(1)

# url_parts = list(urlparse.urlparse(url))

# query = dict(urlparse.parse_qsl(url_parts[4]))

# d1 = {"date": prev_date_param}
# query.update(d1)

# url_parts[4] = urlencode(query)

# received_data = requests.get(url = url)
# received_data = received_data.json()

# data = received_data["data"]
# cyber_city_data = data["dlf_cyber_city"]

# cyber_city_object = cyber_city_data[0]

# cyber_city_median_price = cyber_city_object["median_price"]

# print(cyber_city_median_price)

# # print(urlparse.urlunparse(url_parts))


# import math
# import json
# import requests
# import datetime
# import numpy as np
# import urllib.parse as urlparse
# from urllib.parse import urlencode

# url = "https://api.nodal.direct/v1/index.php/Api/getDynamicPriceWithDate?date=2019-09-2"
# prev_date_param = datetime.date.today()-datetime.timedelta(1)


# url_parts = list(urlparse.urlparse(url))
# query = dict(urlparse.parse_qsl(url_parts[4]))
# d1 = {"date": prev_date_param}
# query.update(d1)
# url_parts[4] = urlencode(query)
# url_parts[3] = "?"
# url_parts[0] = "https://"

# query_string = ""

# for i in url_parts:
#     query_string += i

# print(url_parts)

# received_data = requests.get(url = url)
# received_data_json = received_data.json()
# print(received_data_json)

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

url_list = ['https://www.oyorooms.com/search?checkin=03%2F10%2F2019&checkout=04%2F10%2F2019&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.471981&filters%5Bcoordinates%5D%5Blongitude%5D=77.104735&filters%5Broom_pricing%5D%5Bmax%5D=3701&filters%5Broom_pricing%5D%5Bmin%5D=2302&guests=2&latitude=28.471981&location=DLF+Phase+1%2C+Gurgaon%2C+Haryana&longitude=77.104735&roomConfig%5B%5D=2&rooms=1&searchType=locality&showSearchElements=false',
                'https://www.oyorooms.com/search?checkin=03%2F10%2F2019&checkout=04%2F10%2F2019&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.4949762&filters%5Bcoordinates%5D%5Blongitude%5D=77.0895421&filters%5Broom_pricing%5D%5Bmax%5D=2611&filters%5Broom_pricing%5D%5Bmin%5D=1809&guests=2&latitude=28.4949762&location=Dlf+Cyber+City%2C+Gurugram%2C+Haryana&longitude=77.0895421&roomConfig%5B%5D=2&rooms=1&searchType=locality&showSearchElements=false',
                'https://www.oyorooms.com/search?checkin=03%2F10%2F2019&checkout=04%2F10%2F2019&country=india&coupon=&filters%5Bcoordinates%5D%5Blatitude%5D=28.45911&filters%5Bcoordinates%5D%5Blongitude%5D=77.07255&filters%5Broom_pricing%5D%5Bmax%5D=3708&filters%5Broom_pricing%5D%5Bmin%5D=2312&guests=2&latitude=28.45911&location=Huda+City+Center+Metro%2C+Gurugram%2C+Haryana&longitude=77.07255&roomConfig%5B%5D=2&rooms=1&searchType=locality&showSearchElements=false'
                ]
                
combined_list = []
filename = 'test.csv'

column_header = ['Name', 'Price', 'Region', 'Date'] 

with open(filename, 'w') as write_file:
    writer = csv.writer(write_file)
    writer.writerow(column_header)
write_file.close()

for url in url_list:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_range = [a.get_text() for a in soup.find_all('span', {"class": "input-range__label-container"})]

    print(price_range[1])
    print(price_range[2])