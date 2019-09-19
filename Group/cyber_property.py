from surge_price import get_surge_price
from base_price import cyber_base_price
from data import cyber_city_total_rooms, cyber_property_name

def _cyber_city_(i, j, cyber_surge_index, cyber_data_dict={}):
        
        cyber_data_dict["property_name"] = 'arbor_cyber_city'
        total_avail_rooms = i.cell(j, 17).value
        cyber_city_current_occ_percentage = 100 - ((total_avail_rooms/cyber_city_total_rooms) * 100)

        if cyber_city_current_occ_percentage > cyber_surge_index:
                cyber_data_dict = get_surge_price(cyber_city_current_occ_percentage, cyber_surge_index, cyber_property_name, cyber_data_dict)

        else:
                cyber_data_dict["cyber_city_price"] = cyber_base_price

        print(cyber_data_dict)
        print("-------")