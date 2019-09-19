import json
import requests
import datetime

from single_surge import surge_arbor_price, surge_golf_course_price, surge_cyber_city_price
from double_surge import double_surge_arbor_price, double_surge_cyber_city_price, double_surge_golf_course_price
from triple_surge import triple_surge_arbor_price, triple_surge_cyber_city_price, triple_surge_golf_course_price
from quad_surge import quad_surge_arbor_price, quad_surge_cyber_city_price, quad_surge_golf_course_price
from poly_surge import poly_surge_arbor_price, poly_surge_cyber_city_price, poly_surge_golf_course_price

from data import arbor_base_price, golf_base_price, cyber_base_price, perch_arbor_property_name, golf_course_property_name, cyber_property_name
from base_price import set_base_arbor_price, set_base_cyber_city_price, set_base_golf_course_price

def set_base_price(prop_name, property_data_dict={}):

    if prop_name == perch_arbor_property_name:
        property_data_dict = set_base_arbor_price(property_data_dict)

    elif prop_name == golf_course_property_name:
        property_data_dict = set_base_golf_course_price(property_data_dict)
        
    elif prop_name == cyber_property_name:
        property_data_dict = set_base_cyber_city_price(property_data_dict)

    return property_data_dict

def get_surge_price(occupancy_percentage, surge_index, prop_name, property_data_dict={}):

    todays_date = datetime.date.today()

    receive_here = "https://api.nodal.direct/v1/index.php/Api/getDynamicPrice"
    received_data = requests.get(url = receive_here)
    all_oyo_data = received_data.json()

    if all_oyo_data["status"] == 400:
            print("Get oyo data request error")
    
    else:
        all_oyo_data =  all_oyo_data["data"]
        get_prop_data = all_oyo_data["{}".format(prop_name.strip())]

        for i in all_oyo_data:
            if str(prop_name).strip() == str(i).strip():
                if abs(surge_index - occupancy_percentage) > 1 and abs(surge_index - occupancy_percentage) <= 11:
                    try:
                        for item in get_prop_data:
                            date = item["date"]
                            data_date = date[:10]

                            if str(todays_date).strip() == str(data_date).strip():
                                oyo_med_price = item["median_price"]
                                price_index = item["price_index"]
                                if oyo_med_price > arbor_base_price and prop_name.strip() == perch_arbor_property_name.strip():
                                    property_data_dict = surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                                elif oyo_med_price > golf_base_price and prop_name.strip() == golf_course_property_name.strip():
                                    property_data_dict = surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                                elif oyo_med_price > cyber_base_price and prop_name.strip() == cyber_property_name.strip():
                                    property_data_dict = surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                                else:
                                    property_data_dict = set_base_price(prop_name, property_data_dict)

                            else:
                                pass

                    except Exception:
                        print("Missing todays OYO data in surge")

                elif abs(surge_index - occupancy_percentage) > 11 and abs(surge_index - occupancy_percentage) <=21:
                    try:
                        for item in get_prop_data:
                            date = item["date"]
                            data_date = date[:10]
                            if str(todays_date).strip() == str(data_date).strip():
                                oyo_med_price = item["median_price"]
                                price_index = item["price_index"]
                                if oyo_med_price > arbor_base_price and prop_name.strip() == perch_arbor_property_name.strip():
                                    property_data_dict = double_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                                elif oyo_med_price > golf_base_price and prop_name.strip() == golf_course_property_name.strip():
                                    property_data_dict = double_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                                elif oyo_med_price > cyber_base_price and prop_name.strip() == cyber_property_name.strip():
                                    property_data_dict = double_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                                else:
                                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

                            else:
                                pass

                    except Exception:
                        print("Missing todays OYO data in double surge")

                elif abs(surge_index - occupancy_percentage) > 21 and abs(surge_index - occupancy_percentage) <= 31:
                    try:
                        for item in get_prop_data:
                            date = item["date"]
                            data_date = date[:10]
                            if str(todays_date).strip() == str(data_date).strip():
                                oyo_med_price = item["median_price"]
                                price_index = item["price_index"]

                                if oyo_med_price > arbor_base_price and prop_name.strip() == perch_arbor_property_name.strip():
                                    property_data_dict = triple_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                                elif oyo_med_price > golf_base_price and prop_name.strip() == golf_course_property_name.strip():
                                    property_data_dict = triple_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                                elif oyo_med_price > cyber_base_price and prop_name.strip() == cyber_property_name.strip():
                                    property_data_dict = triple_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                                else:
                                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

                            else:
                                pass

                    except Exception:
                        print("Missing todays OYO data in triple surge")

                elif abs(surge_index - occupancy_percentage) > 31 and abs(surge_index - occupancy_percentage) <= 41:
                    try:
                        for item in get_prop_data:
                            date = item["date"]
                            data_date = date[:10]
                            if str(todays_date).strip() == str(data_date).strip():
                                oyo_med_price = item["median_price"]
                                price_index = item["price_index"]

                                if oyo_med_price > arbor_base_price and prop_name.strip() == perch_arbor_property_name.strip():
                                    property_data_dict = quad_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                                elif oyo_med_price > golf_base_price and prop_name.strip() == golf_course_property_name.strip():
                                    property_data_dict = quad_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                                elif oyo_med_price > cyber_base_price and prop_name.strip() == cyber_property_name.strip():
                                    property_data_dict = quad_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                                else:
                                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

                            else:
                                pass

                    except Exception:
                        print("Missing todays OYO data in quad surge")

                else:
                    try:
                        for item in get_prop_data:
                            date = item["date"]
                            data_date = date[:10]
                            if str(todays_date).strip() == str(data_date).strip():
                                oyo_med_price = item["median_price"]
                                price_index = item["price_index"]
                                if oyo_med_price > arbor_base_price and prop_name.strip() == perch_arbor_property_name.strip():
                                    property_data_dict = poly_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                                elif oyo_med_price > golf_base_price and prop_name.strip() == golf_course_property_name.strip():
                                    property_data_dict = poly_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                                elif oyo_med_price > cyber_base_price and prop_name.strip() == cyber_property_name.strip():
                                    property_data_dict = poly_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                                else:
                                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

                            else:
                                pass

                    except Exception:
                        print("Missing todays OYO data in poly surge")

            else:
                print("No property to assign surge price")

        return property_data_dict