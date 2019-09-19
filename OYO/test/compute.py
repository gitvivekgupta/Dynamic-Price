import math
import numpy as np

dlf_data_dict = {}
cyber_data_dict = {}
huda_data_dict = {}

def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

def compute_dlf(dlf_data):

    avg_price = dlf_data['Price'].mean()
    max_price = dlf_data['Price'].max()
    min_price = dlf_data['Price'].min()
    price_index = 100 + (max_price/min_price)
    median_price = dlf_data['Price'].median()
    std_dev = dlf_data['Price'].std()
    tenth_percentile = np.percentile(dlf_data['Price'], [10])
    nintyth_percentile = np.percentile(dlf_data['Price'], [90])

    dlf_data_dict["region"] = 'dlf_phase1'
    dlf_data_dict["avg_price"] = math.floor(avg_price)
    dlf_data_dict["median_price"] = math.floor(median_price)
    dlf_data_dict["std_deviation"] = math.floor(std_dev)
    dlf_data_dict["tenth_percentile"] = math.floor(tenth_percentile)
    dlf_data_dict["nineth_percentile"] = math.floor(nintyth_percentile)
    dlf_data_dict["price_index"] = round(price_index, 2)

    return dlf_data_dict

def compute_cyber(cyber_data):

    dlf_data_dict["region"] = 'dlf_cyber_city'
    avg_price = cyber_data['Price'].mean()
    max_price = cyber_data['Price'].max()
    min_price = cyber_data['Price'].min()
    price_index = 100 + (max_price/min_price)
    median_price = cyber_data['Price'].median()
    std_dev = cyber_data['Price'].std()
    # variance = df['Price'].var()
    tenth_percentile = np.percentile(cyber_data['Price'], [10])
    nintyth_percentile = np.percentile(cyber_data['Price'], [90])

    cyber_data_dict["avg_price"] = math.floor(avg_price)
    cyber_data_dict["median_price"] = math.floor(median_price)
    cyber_data_dict["std_deviation"] = math.floor(std_dev)
    cyber_data_dict["tenth_percentile"] = math.floor(tenth_percentile)
    cyber_data_dict["nineth_percentile"] = math.floor(nintyth_percentile)
    cyber_data_dict["price_index"] = round(price_index, 2)

    return cyber_data_dict

def compute_huda(huda_data):

    dlf_data_dict["region"] = 'huda_city_center'
    avg_price = huda_data['Price'].mean()
    max_price = huda_data['Price'].max()
    min_price = huda_data['Price'].min()
    # variance = df['Price'].var()
    median_price = huda_data['Price'].median()
    price_index = 100 + (max_price/min_price)
    std_dev = huda_data['Price'].std()
    tenth_percentile = np.percentile(huda_data['Price'], [10])
    nintyth_percentile = np.percentile(huda_data['Price'], [90])

    huda_data_dict["avg_price"] = math.floor(avg_price)
    huda_data_dict["median_price"] = math.floor(median_price)
    huda_data_dict["std_deviation"] = math.floor(std_dev)
    huda_data_dict["tenth_percentile"] = math.floor(tenth_percentile)
    huda_data_dict["nineth_percentile"] = math.floor(nintyth_percentile)
    huda_data_dict["price_index"] = round(price_index, 2)

    return huda_data_dict