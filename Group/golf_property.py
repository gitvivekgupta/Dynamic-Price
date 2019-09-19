from surge_price import get_surge_price
from base_price import golf_base_price
from data import golf_course_road_total_rooms, golf_course_property_name

def _golf_course_(i, j, golf_surge_index, golf_data_dict = {}):

        golf_data_dict["property_name"] = golf_course_property_name
        total_avail_rooms = i.cell(j, 11).value
        golf_course_current_occ_percentage = 100 - ((total_avail_rooms/golf_course_road_total_rooms) * 100)

        if golf_course_current_occ_percentage > golf_surge_index:
            golf_data_dict = get_surge_price(golf_course_current_occ_percentage, golf_surge_index, golf_course_property_name, golf_data_dict)

        else:
                golf_data_dict["golf_course_price"] = golf_base_price

        print(golf_data_dict)
        print("-------")