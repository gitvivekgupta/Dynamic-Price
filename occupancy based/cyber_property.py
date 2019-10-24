import time
import json

from dates import todays_date
from surge_price import get_surge_price
from base_price import set_base_cyber_city_price
from data import cyber_city_total_rooms, cyber_property_name

cyber_final_list = []

def _cyber_city_(i, j, cyber_surge_index, forecast_date):

        cyber_data_dict = {}
        
        cyber_data_dict["property_name"] = str(cyber_property_name)
        cyber_data_dict["date"] = forecast_date

        total_avail_rooms = i.cell(j, 17).value
        cyber_city_current_occ_percentage = 100 - ((int(total_avail_rooms)/int(cyber_city_total_rooms)) * 100)
        cyber_city_current_occ_percentage = round(cyber_city_current_occ_percentage, 2)

        if cyber_city_current_occ_percentage > cyber_surge_index:
                
                cyber_data_dict = get_surge_price(cyber_city_current_occ_percentage, cyber_surge_index, cyber_property_name, cyber_data_dict)

        else:
                cyber_data_dict = set_base_cyber_city_price(cyber_data_dict)

        cyber_final_list.append(cyber_data_dict)