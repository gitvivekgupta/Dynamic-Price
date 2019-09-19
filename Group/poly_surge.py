from data import cyber_max_price, golf_max_price, arbor_max_price

def poly_surge_arbor_price(oyo_med_price, base_price, price_index, property_data_dict={}):

    if price_index < 100:

        if oyo_med_price < base_price:
            property_data_dict["arbor_price"] = base_price

        else:
            if oyo_med_price < arbor_max_price:
                property_data_dict["arbor_price"] = oyo_med_price

            else:
                property_data_dict["arbor_price"] = arbor_max_price

    else:
        price_index = (price_index/100) * 1.5
        assign_arbor_price = oyo_med_price * price_index

        if assign_arbor_price < arbor_max_price: 
            property_data_dict["arbor_price"] = assign_arbor_price
        
        else:
            property_data_dict["arbor_price"] = arbor_max_price

    return property_data_dict

def poly_surge_golf_course_price(oyo_med_price, base_price, price_index, property_data_dict={}):

    if price_index < 100:

        if oyo_med_price < base_price:
            property_data_dict["golf_course_price"] = base_price
        else:
            if oyo_med_price < golf_max_price:
                property_data_dict["golf_course_price"] = oyo_med_price

            else:
                property_data_dict["golf_course_price"] = golf_max_price

    else:
        price_index = (price_index/100) * 1.5
        assign_golf_price = oyo_med_price * price_index

        if assign_golf_price < golf_max_price:
            property_data_dict["golf_course_price"] = assign_golf_price

        else:
            property_data_dict["golf_course_price"] = golf_max_price

    return property_data_dict

def poly_surge_cyber_city_price(oyo_med_price, base_price, price_index, property_data_dict={}):

    if price_index < 100:

        if oyo_med_price < base_price:
            property_data_dict["cyber_city_price"] = base_price
        else:
            if oyo_med_price < cyber_max_price:
                property_data_dict["cyber_city_price"] = oyo_med_price
            
            else:
                property_data_dict["cyber_city_price"] = oyo_med_price
    
    else:
        price_index = (price_index/100) * 1.5
        assign_cyber_price = oyo_med_price * price_index

        if assign_cyber_price < cyber_max_price:
            property_data_dict["cyber_city_price"] = assign_cyber_price

        else:
            property_data_dict["cyber_city_price"] = cyber_max_price

    return property_data_dict