import time
import json

from surge_price import get_surge_price
from base_price import set_base_golf_course_price
from data import golf_course_road_total_rooms, golf_course_property_name

golf_final_list = []

def _golf_course_(i, j, golf_surge_index, forecast_date):

        golf_data_dict = {}

        golf_data_dict["property_name"] = str(golf_course_property_name)
        golf_data_dict["date"] = forecast_date
        
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        golf_data_dict["time"] = current_time

        total_avail_rooms = i.cell(j, 11).value
        golf_course_current_occ_percentage = 100 - ((int(total_avail_rooms)/int(golf_course_road_total_rooms)) * 100)
        golf_course_current_occ_percentage = round(golf_course_current_occ_percentage, 2)

        if golf_course_current_occ_percentage > golf_surge_index:

                golf_data_dict = get_surge_price(golf_course_current_occ_percentage, golf_surge_index, golf_course_property_name, golf_data_dict)

        else:
                golf_data_dict = set_base_golf_course_price(golf_data_dict)

        golf_data_json = json.dumps(golf_data_dict)
        golf_final_list.append(golf_data_json)

        # print(golf_data_json)
