import json
import requests
from scrap_oyo import scrap_oyo

receive_here = 'https://api.nodal.direct/v1/index.php/Api/getDynamicPrice'

received_data = requests.get(url = receive_here)
data = received_data.json()

access =  data["data"]

# data_access = access["dlf_phase_1"]

# for i in data_access:
#     print(i)

# for i in access:
#     print(i)

# print(access)

print(access)