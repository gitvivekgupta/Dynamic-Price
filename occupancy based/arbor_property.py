import time
import json
from dates import todays_date
from surge_price import get_surge_price
from base_price import set_base_arbor_price
from data import arbor_suites_total_rooms, perch_arbor_property_name

arbor_final_list = []

def _perch_arbor_suites_(i, j, arbor_surge_index, forecast_date):

        arbor_data_dict = {}
        arbor_data_dict["property_name"] = str(perch_arbor_property_name)
        arbor_data_dict["date"] = forecast_date

        total_avail_rooms = i.cell(j, 5).value
        arbor_suites_current_occ_percentage = 100 - ((int(total_avail_rooms)/int(arbor_suites_total_rooms)) * 100)
        arbor_suites_current_occ_percentage = round(arbor_suites_current_occ_percentage, 2)

        if arbor_suites_current_occ_percentage > arbor_surge_index:
                
                arbor_data_dict = get_surge_price(arbor_suites_current_occ_percentage, arbor_surge_index, perch_arbor_property_name, arbor_data_dict)

        else:
                arbor_data_dict = set_base_arbor_price(arbor_data_dict)

        arbor_final_list.append(arbor_data_dict)
        
