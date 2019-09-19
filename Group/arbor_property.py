from surge_price import get_surge_price
from base_price import arbor_base_price
from data import arbor_suites_total_rooms, perch_arbor_property_name

def _perch_arbor_suites_(i, j, arbor_surge_index, arbor_data_dict={}):
        
        arbor_data_dict["property_name"] = perch_arbor_property_name
        total_avail_rooms = i.cell(j, 5).value
        arbor_suites_current_occ_percentage = 100 - ((total_avail_rooms/arbor_suites_total_rooms) * 100)

        if arbor_suites_current_occ_percentage > arbor_surge_index:
                arbor_data_dict = get_surge_price(arbor_suites_current_occ_percentage, arbor_surge_index, perch_arbor_property_name, arbor_data_dict)

        else:
                arbor_data_dict["arbor_price"] = arbor_base_price

        print(arbor_data_dict)
        print("-------")