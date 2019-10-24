import json
import requests
from scrap_oyo import scrap_oyo

all_data = {}

all_data = scrap_oyo(all_data)

myjson = json.dumps({"data":all_data})

print(myjson)

send_here = "https://api.nodal.direct/v1/index.php/Api/DynamicPrice"

data_sent = requests.post(url = send_here, data = myjson) 

pastebin_url = data_sent.text 
print(pastebin_url)