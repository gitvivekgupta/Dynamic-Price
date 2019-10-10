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

    if str(prop_name).strip() == str(perch_arbor_property_name).strip():
        property_data_dict = set_base_arbor_price(property_data_dict)

    elif str(prop_name).strip() == str(golf_course_property_name).strip():
        property_data_dict = set_base_golf_course_price(property_data_dict)
        
    elif str(prop_name).strip() == str(cyber_property_name).strip():
        property_data_dict = set_base_cyber_city_price(property_data_dict)

    return property_data_dict

def get_surge_price(occupancy_percentage, surge_index, prop_name, property_data_dict={}):

    # print("---")
    # print(prop_name)
    # print("---")

    todays_date = datetime.date.today() + datetime.timedelta(days=0)
    todays_date = todays_date.strftime("%Y-%m-%d")

    receive_here = "https://api.nodal.direct/v1/index.php/Api/getDynamicPrice"
    received_data = requests.get(url = receive_here)
    all_oyo_data = received_data.json()

    if all_oyo_data["status"] == 400:
        print("Get oyo data api request error")
    
    else:

        all_oyo_data =  all_oyo_data["data"]
        get_prop_data = all_oyo_data["{}".format(prop_name.strip())]

        get_prop_data_last = get_prop_data[-1]

        date = get_prop_data_last["date"]
        data_date = date[:10]

        oyo_med_price = float(get_prop_data_last["median_price"])
        price_index = float(get_prop_data_last["price_index"])

        if occupancy_percentage - surge_index > 1 and occupancy_percentage - surge_index <= 11:

            # print("single surge")

            if str(todays_date).strip() == str(data_date).strip():

                if oyo_med_price > arbor_base_price and str(prop_name).strip() == str(perch_arbor_property_name).strip():
                    property_data_dict = surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)
                
                elif oyo_med_price > golf_base_price and str(prop_name).strip() == str(golf_course_property_name).strip():
                    property_data_dict = surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)
                
                elif oyo_med_price > cyber_base_price and str(prop_name).strip() == str(cyber_property_name).strip():
                    property_data_dict = surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)
                
                else:
                    property_data_dict = set_base_price(prop_name, property_data_dict)
            
            else:
                print("Missing todays OYO data in single surge")
                pass

        elif occupancy_percentage - surge_index > 11 and occupancy_percentage - surge_index <=21:

            # print("double surge")

            if str(todays_date).strip() == str(data_date).strip():

                if oyo_med_price > arbor_base_price and str(prop_name).strip() == str(perch_arbor_property_name).strip():
                    property_data_dict = double_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                elif oyo_med_price > golf_base_price and str(prop_name).strip() == str(golf_course_property_name).strip():
                    property_data_dict = double_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                elif oyo_med_price > cyber_base_price and str(prop_name).strip() == str(cyber_property_name).strip():
                    property_data_dict = double_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                else:
                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

            else:
                print("Missing todays OYO data in double surge")
                pass

        elif occupancy_percentage - surge_index > 21 and occupancy_percentage - surge_index <= 31:

            # print("triple surge")

            if str(todays_date).strip() == str(data_date).strip():

                if oyo_med_price > arbor_base_price and str(prop_name).strip() == str(perch_arbor_property_name).strip():
                    property_data_dict = triple_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                elif oyo_med_price > golf_base_price and str(prop_name).strip() == str(golf_course_property_name).strip():
                    property_data_dict = triple_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                elif oyo_med_price > cyber_base_price and str(prop_name).strip() == str(cyber_property_name).strip():
                    property_data_dict = triple_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                else:
                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

            else:
                print("Missing todays OYO data in triple surge")
                pass

        elif occupancy_percentage - surge_index > 31 and occupancy_percentage - surge_index <= 41:

            # print("quad surge")

            if str(todays_date).strip() == str(data_date).strip():

                if oyo_med_price > arbor_base_price and str(prop_name).strip() == str(perch_arbor_property_name).strip():
                    property_data_dict = quad_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                elif oyo_med_price > golf_base_price and str(prop_name).strip() == str(golf_course_property_name).strip():
                    property_data_dict = quad_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                elif oyo_med_price > cyber_base_price and str(prop_name).strip() == str(cyber_property_name).strip():
                    property_data_dict = quad_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)

                else:
                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

            else:
                print("Missing todays OYO data in triple surge")
                pass

        else:

            # print("poly surge")
            
            if str(todays_date).strip() == str(data_date).strip():

                if oyo_med_price > arbor_base_price and str(prop_name).strip() == str(perch_arbor_property_name).strip():
                    property_data_dict = poly_surge_arbor_price(oyo_med_price, arbor_base_price, price_index, property_data_dict)

                elif oyo_med_price > golf_base_price and str(prop_name).strip() == str(golf_course_property_name).strip():
                    property_data_dict = poly_surge_golf_course_price(oyo_med_price, golf_base_price, price_index, property_data_dict)

                elif oyo_med_price > cyber_base_price and str(prop_name).strip() == str(cyber_property_name).strip():
                    property_data_dict = poly_surge_cyber_city_price(oyo_med_price, cyber_base_price, price_index, property_data_dict)
                    
                else:
                    property_data_dict = property_data_dict = set_base_price(prop_name, property_data_dict)

            else:
                print("Missing todays OYO data in poly surge")
                pass

    return property_data_dict