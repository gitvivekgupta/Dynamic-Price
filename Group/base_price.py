from data import arbor_base_price, golf_base_price, cyber_base_price
from data import arbor_max_price, golf_max_price, cyber_max_price

def set_base_arbor_price(data_dict={}):

    data_dict["price"] = arbor_base_price
    return data_dict

def set_base_golf_course_price(data_dict={}):

    data_dict["price"] = golf_base_price
    return data_dict

def set_base_cyber_city_price(data_dict={}):

    data_dict["price"] = cyber_base_price
    return data_dict