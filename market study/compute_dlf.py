import math
import requests
import datetime
import numpy as np
import urllib.parse as urlparse

from urllib.parse import urlencode

def compute_dlf_avg(dlf_data):
    avg_price = round(dlf_data['Price'].mean(), 2)
    return avg_price

def compute_dlf_index(todays_median):

    url = "https://api.nodal.direct/v1/index.php/Api/getDynamicPriceWithDate?date=2019-08-26"

    prev_date_param = datetime.date.today()-datetime.timedelta(1)
    
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    d1 = {"date": prev_date_param}
    query.update(d1)

    url_parts[4] = urlencode(query)
    url_parts[3] = "?"
    url_parts[0] = "https://"

    query_string = ""

    for i in url_parts:
        query_string += i

    received_data = requests.get(url = query_string)
    received_data_json = received_data.json()

    data = received_data_json["data"]
    cyber_city_data = data["dlf_phase_1"]
    cyber_city_object = cyber_city_data[0]
    prev_day_median = cyber_city_object["median_price"]
    index = (float(todays_median)/float(prev_day_median))*100
    price_index = round(index, 2)

    return price_index

def compute_dlf_median(dlf_data):
    median_price = round(dlf_data['Price'].median(), 2)
    return median_price

def compute_dlf_std(dlf_data):
    std_dev = round(dlf_data['Price'].std(), 2)
    return std_dev

def compute_dlf_ten_percentile(dlf_data):
    tenth_percentile = round(np.percentile(dlf_data['Price'], 10), 2)
    return tenth_percentile

def compute_dlf_nine_percentile(dlf_data):
    nintyth_percentile = round(np.percentile(dlf_data['Price'], 90), 2)
    return nintyth_percentile