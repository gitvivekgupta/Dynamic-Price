import math
import numpy as np


def compute_cyber_avg(dlf_data):
    avg_price = round(dlf_data['Price'].mean(), 2)
    return avg_price

def compute_cyber_index(dlf_data):
    min_price = dlf_data['Price'].min()
    max_price = dlf_data['Price'].max()
    price_index = round(100 + (max_price/min_price), 2) 
    return price_index

def compute_cyber_median(dlf_data):
    median_price = round(dlf_data['Price'].median(), 2)
    return median_price

def compute_cyber_std(dlf_data):
    std_dev = round(dlf_data['Price'].std(), 2)
    return std_dev

def compute_cyber_ten_percentile(dlf_data):
    tenth_percentile = round(np.percentile(dlf_data['Price'], 10), 2)
    return tenth_percentile

def compute_cyber_nine_percentile(dlf_data):
    nintyth_percentile = round(np.percentile(dlf_data['Price'], 90), 2)
    return nintyth_percentile
