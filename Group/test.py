
# import requests
# import json
 
# # today = datetime.date.today()
# # print(today)
# # first = today.replace(day=1)
# # print(first)
# # lastMonth = first - datetime.timedelta(days=1)
 
# # print(lastMonth.strftime("%Y-%m"))


# # today = datetime.date.today()
# # todays_date = today.strftime("%d-%b-%y")
# # todays_month = todays_date[3: 6]
# # todays_month = todays_month.upper()

# # this_month_first_date = today.replace(day=1)
# # lastMonth = this_month_first_date - datetime.timedelta(days=1)
# # lastMonth = lastMonth.strftime("%b")

# # print(lastMonth)

# # receive_here = "https://api.nodal.direct/v1/index.php/Api/GroupDynamicPrice"
# # received_data = requests.get(url = receive_here)
# # data = received_data.json()
# # print(data)

# # arr = []

# # receive_here = "https://api.nodal.direct/v1/index.php/Api/getGroupDynamicPrice"
# # received_data = requests.get(url = receive_here)
# # data = received_data.json()

# # print(data)
# # ar = data["status"]
# # print(ar)

# # arr = data["data"]

# # for i in arr:
# #     print(i["arbor_suites_med_occ"])

# post_data = {}

# post_data["month"] = 'AUG'
# post_data["arbor_suites_med_occ"] = 606
# post_data["golf_course_med_occ"] = 504
# post_data["cyber_city_med_occ"] = 404

# print(post_data)

# post_data_json = json.dumps(post_data)

# send_here = "https://api.nodal.direct/v1/index.php/Api/GroupDynamicPrice"

# data_sent = requests.post(url = send_here, data = post_data_json) 

# pastebin_url = data_sent.text 
# print(pastebin_url)

# prop_name = "dlf_phase_1"
# receive_here = "https://api.nodal.direct/v1/index.php/Api/getDynamicPrice"
# received_data = requests.get(url = receive_here)
# all_oyo_data = received_data.json()
# all_oyo_data =  all_oyo_data["data"]

# todays_date = datetime.date.today()

# get_prop = all_oyo_data["{}".format(prop_name)]

# for item in get_prop:
#     date = item["date"]
#     data_date = date[:10]

#     if str(todays_date).strip() == str(data_date).strip():
#         print(data_date)

# tomorrows_date = "2019-08-29"

# for item in  get_prop:
#     date = item["date"]
#     date = date[:10]

#     if tomorrows_date == date:
#         print(date)
#     else:
#         print("not found")


# today = datetime.date.today() + datetime.timedelta(days=1)
# todays_date = today.strftime("%d-%b-%y")
# print(todays_date)

# todays_date = datetime.date.today()
# tomorrows_date = datetime.date.today() + datetime.timedelta(days=1)
# todays_date = todays_date.strftime("%d-%b-%y")


# tomorrows_date = datetime.date.today() + datetime.timedelta(days=2)
# tomorrows_date = tomorrows_date.strftime("%d-%b-%y")

# print(tomorrows_date)
# arbor_data_dict = {}

# prop_name = 'perch_arbor_suites'

# arbor_data_dict["prop_one_name"] = prop_name
# arbor_data_dict["arbor_price"] = 5434

# print(arbor_data_dict)

# receive_median_occ_here = "https://api.nodal.direct/v1/index.php/Api/getGroupDynamicPrice"
# received_data = requests.get(url = receive_median_occ_here)
# spreadsheet_api_data = received_data.json()
# api_arr = spreadsheet_api_data["data"]
            
# for j in api_arr:
#     month_from_db = j["month"]

# print(month_from_db)

# import gspread
# import statistics

# from oauth2client.service_account import ServiceAccountCredentials
# from pprint import pprint
# from datetime import date

# scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
# client = gspread.authorize(creds)
# sheet = client.open("(2019) GROUP OCCUPANCY")

# for i in sheet:
#     one_week_one = i.cell(10, 6).value
#     one_week_one = one_week_one[:5]
#     break
# print(one_week_one)

# four_week_one = i.cell(10, 23).value
# four_week_two = i.cell(17, 23).value
# four_week_three = i.cell(24, 23).value
# four_week_four = i.cell(33, 23).valu
# five_week_one = i.cell(10, 28).value
# five_week_two = i.cell(17, 28).value
# five_week_three = i.cell(24, 28).value
# five_week_four = i.cell(33, 28).value







































    # jan = current_sheet.find('JAN')
    # feb = current_sheet.find('FEB')
    # mar = current_sheet.find('MAR')
    # apr = current_sheet.find('APR')
    # may = current_sheet.find('MAY')
    # jun = current_sheet.find('JUN')
    # jul = current_sheet.find('JUL')
    # aug = current_sheet.find('AUG')
    # sep = current_sheet.find('SEP')
    # octo = current_sheet.find('OCT')
    # nov = current_sheet.find('NOV')
    # dec = current_sheet.find('DEC')

#     if jan != -1:

#         data_dict["data"]["month"] = 'jan'
#         get_data(i, data_dict)

#     elif feb != -1:

#         data_dict["data"]["month"] = 'feb'
#         get_data(i, data_dict)

#     elif mar != -1:

#         data_dict["data"]["month"] = 'mar'
#         get_data(i, data_dict)

#     elif apr != -1:

#         data_dict["data"]["month"] = 'apr'
#         get_data(i, data_dict)

#     elif may != -1:

#         data_dict["data"]["month"] = 'may'
#         get_data(i, data_dict)

#     elif jun != -1:

#         data_dict["data"]["month"] = 'jun'
#         get_data(i, data_dict)

#     elif jul != -1:

#         data_dict["data"]["month"] = 'jul'
#         get_data(i, data_dict)

#     elif aug != -1:

#         data_dict["data"]["month"] = 'aug'
#         get_data(i, data_dict)

#     elif sep != -1:

#         data_dict["data"]["month"] = 'sep'
#         get_data(i, data_dict)

#     elif octo != -1:

#         data_dict["data"]["month"] = 'oct'
#         get_data(i, data_dict)

#     elif nov != -1:

#         data_dict["data"]["month"] = 'nov'
#         get_data(i, data_dict)

#     elif dec != -1:

#         data_dict["data"]["month"] = 'dec'
#         get_data(i, data_dict)

#     else:
#         pass

# print(data_dict)

    # print(property_one, one_week_one, one_week_two, one_week_three, one_week_four)
    # print(property_two, two_week_one, two_week_two, two_week_three, two_week_four)
    # print(property_three, three_week_one, three_week_two, three_week_three, three_week_four)
    # print(property_four, four_week_one, four_week_two, four_week_three, four_week_four)
    # print(property_five, five_week_one, five_week_two, five_week_three, five_week_four)


























# four_week_one = i.cell(10, 23).value
# four_week_two = i.cell(17, 23).value
# four_week_three = i.cell(24, 23).value
# four_week_four = i.cell(33, 23).valu
# five_week_one = i.cell(10, 28).value
# five_week_two = i.cell(17, 28).value
# five_week_three = i.cell(24, 28).value
# five_week_four = i.cell(33, 28).value
















        
# data_dict["data"]["prop_one_week1"] = one_week_one
# data_dict["data"]["prop_one_week2"] = one_week_two
# data_dict["data"]["prop_one_week3"] = one_week_three
# data_dict["data"]["prop_one_week4"] = one_week_four

# data_dict["data"]["prop_two_week1"] = two_week_one
# data_dict["data"]["prop_two_week2"] = two_week_two
# data_dict["data"]["prop_two_week3"] = two_week_three
# data_dict["data"]["prop_two_week4"] = two_week_four

# data_dict["data"]["prop_three_week1"] = three_week_one
# data_dict["data"]["prop_three_week2"] = three_week_two
# data_dict["data"]["prop_three_week3"] = three_week_three
# data_dict["data"]["prop_three_week4"] = three_week_four

# data_dict["data"]["prop_four_name"] = 'arbor_cyber_city
# data_dict["data"]["prop_four_week1"] = four_week_one
# data_dict["data"]["prop_four_week2"] = four_week_two
# data_dict["data"]["prop_four_week3"] = four_week_three
# data_dict["data"]["prop_four_week4"] = four_week_four

# data_dict["data"]["prop_five_name"] = 'perch_grov
# data_dict["data"]["prop_five_week1"] = five_week_one
# data_dict["data"]["prop_five_week2"] = five_week_two
# data_dict["data"]["prop_five_week3"] = five_week_three
# data_dict["data"]["prop_five_week4"] = five_week_four

# property_one_name = i.cell(2, 2).value
# property_two_name = i.cell(2, 8).value
# property_three_name = i.cell(2, 14).value
# property_four_name = i.cell(2, 21).value
# property_five_name = i.cell(2, 26).value

# import datetime

# tomorrows_date_for_last_month = datetime.date.today() + datetime.timedelta(days=1)

# this_month_first_date = tomorrows_date_for_last_month.replace(day=1)
# last_month = this_month_first_date - datetime.timedelta(days=1)
# last_month = last_month.strftime("%b")

# print(last_month)

# import re
# import json
# import gspread
# import datetime
# import requests

# from pprint import pprint
# from get_median_occ import median_occupancy
# from oauth2client.service_account import ServiceAccountCredentials
# from dates import tomorrows_date, tomorrows_date_month, day_after_tomorrows_date, day_after_tomorrows_month, two_days_after_tomorrows_date, two_days_after_tomorrows_month

# scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
# client = gspread.authorize(creds)
# sheet = client.open("(2019) GROUP OCCUPANCY")

# for i in sheet:

#     i_str = str(i)
#     sheet_month = re.findall(r"'(.*?)'", i_str)
#     sheet_month = sheet_month[0]
#     sheet_month = sheet_month[:3]
    

#     if str(sheet_month).strip() == str(tomorrows_date_month).strip() and str(sheet_month).strip() == str(day_after_tomorrows_month).strip() and str(sheet_month).strip() == str(two_days_after_tomorrows_month).strip():
#         print(sheet_month)
#         print("---")

#         for j in range(4, 35):

#             sheet_date = i.cell(j, 1)
#             sheet_date = str(sheet_date)
#             sheet_date = re.findall(r"'(.*?)'", sheet_date)
#             sheet_date = sheet_date[0]
#             print(sheet_date)

#         break
# import time
# t = time.localtime()
# current_time = time.strftime("%H:%M", t)
# print(current_time)