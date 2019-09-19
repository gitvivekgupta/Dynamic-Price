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


import math
import json
import requests
import datetime
import numpy as np
import urllib.parse as urlparse
from urllib.parse import urlencode

url = "https://api.nodal.direct/v1/index.php/Api/getDynamicPriceWithDate?date=2019-09-2"
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

print(url_parts)

# received_data = requests.get(url = url)
# received_data_json = received_data.json()
# print(received_data_json)