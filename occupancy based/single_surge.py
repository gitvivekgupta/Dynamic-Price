from data import cyber_max_price, golf_max_price, arbor_max_price

def surge_arbor_price(oyo_med_price, base_price, price_index, property_data_dict={}):

    if price_index < 100:

        if oyo_med_price < base_price:
            property_data_dict["price"] = round(base_price, 2)

        elif oyo_med_price < arbor_max_price and oyo_med_price > base_price:
            property_data_dict["price"] = round(oyo_med_price, 2)

        else:
            property_data_dict["price"] = round(arbor_max_price, 2)

    else:
        
        price_index = price_index/100
        assign_arbor_price = oyo_med_price * price_index

        if assign_arbor_price < arbor_max_price:
            property_data_dict["price"] = round(assign_arbor_price, 2)
        
        else:
            property_data_dict["price"] = round(arbor_max_price, 2)

    return property_data_dict

def surge_golf_course_price(oyo_med_price, base_price, price_index, property_data_dict={}):

    if price_index < 100:

        if oyo_med_price < base_price:
            property_data_dict["price"] = round(base_price, 2)

        elif oyo_med_price < golf_max_price and oyo_med_price > base_price:
                property_data_dict["price"] = round(oyo_med_price, 2)

        else:
            property_data_dict["price"] = round(golf_max_price, 2)

    else:

        price_index = price_index/100
        assign_golf_price = oyo_med_price * price_index

        if assign_golf_price < golf_max_price:
            property_data_dict["price"] = round(assign_golf_price, 2)

        else:
            property_data_dict["price"] = round(golf_max_price, 2)

    return property_data_dict

def surge_cyber_city_price(oyo_med_price, base_price, price_index, property_data_dict={}):

    if price_index < 100:

        if oyo_med_price < base_price:
            property_data_dict["price"] = round(base_price, 2)

        elif oyo_med_price < cyber_max_price and oyo_med_price > base_price:
            property_data_dict["price"] = round(oyo_med_price, 2)
            
        else:
            property_data_dict["price"] = round(cyber_max_price, 2)
    
    else:

        price_index = price_index/100
        assign_cyber_price = oyo_med_price * price_index

        if assign_cyber_price < cyber_max_price:
            property_data_dict["price"] = round(assign_cyber_price, 2)

        else:
            property_data_dict["price"] = round(cyber_max_price, 2)

    return property_data_dict