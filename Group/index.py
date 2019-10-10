import json
import gspread
import datetime
import requests

from pprint import pprint
from get_median_occ import median_occupancy
from oauth2client.service_account import ServiceAccountCredentials
from compute_save import _save_compute_, _save_compute_one_, _save_compute_two_, _save_compute_three_, _save_compute_four_
from dates import todays_date_month, tomorrows_date_month, day_after_tomorrows_month

from arbor_property import arbor_final_list
from golf_property import golf_final_list
from cyber_property import cyber_final_list

def _get_last_month_():

    tomorrows_date_for_last_month = datetime.date.today() + datetime.timedelta(days=1)
    this_month_first_date = tomorrows_date_for_last_month.replace(day=1)
    last_month = this_month_first_date - datetime.timedelta(days=1)
    last_month = last_month.strftime("%b")
    last_month = last_month.upper()

    return last_month

def _store_compute_(i, med_occ, last_month):

    post_data = {}
    med_occ = []

    med_occ = median_occupancy(i, last_month)

    post_data["month"] = todays_date_month
    post_data["arbor_suites_med_occ"] = med_occ[0]
    post_data["golf_course_med_occ"] = med_occ[1]
    post_data["cyber_city_med_occ"] = med_occ[2]
    post_median_occ = json.dumps(post_data)

    send_median_occ_here = "https://api.nodal.direct/v1/index.php/Api/GroupDynamicPrice"
    requests.post(url = send_median_occ_here, data = post_median_occ)

def main():

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("(2019) GROUP OCCUPANCY")

    med_occ = []
    api_arr = []

    receive_median_occ_here = "https://api.nodal.direct/v1/index.php/Api/getGroupDynamicPrice"
    received_data = requests.get(url = receive_median_occ_here)
    spreadsheet_api_data = received_data.json()

    if spreadsheet_api_data["status"] == 400:
        print("get_median_occupancy api request error")

    else:

        for i in sheet:

            api_arr = spreadsheet_api_data["data"]
            api_arr = api_arr[0]
            month_from_db = api_arr["month"]

            if str(todays_date_month).strip() == str(month_from_db).strip() and str(tomorrows_date_month).strip() == str(month_from_db).strip() and str(day_after_tomorrows_month).strip() == str(month_from_db).strip():

                _save_compute_(sheet, api_arr, med_occ)
                print("First condition executed")
                break

            elif str(todays_date_month).strip() != str(month_from_db).strip() and str(tomorrows_date_month).strip() != str(month_from_db).strip() and str(day_after_tomorrows_month).strip() != str(month_from_db).strip():

                last_month = _get_last_month_()
                _store_compute_(i, med_occ, last_month)
                _save_compute_(sheet, api_arr, med_occ)
                print("Second condition executed")
                break

            elif str(todays_date_month).strip() == str(month_from_db).strip() and str(tomorrows_date_month).strip() != str(month_from_db).strip() and str(day_after_tomorrows_month).strip() != str(month_from_db).strip():

                if str(todays_date_month).strip() == str(month_from_db).strip():
                    _save_compute_one_(sheet, api_arr, med_occ)

                elif str(tomorrows_date_month).strip() != str(month_from_db).strip() and str(day_after_tomorrows_month).strip() != str(month_from_db).strip():

                    last_month = _get_last_month_()
                    _store_compute_(i, med_occ, last_month)

                    received_data = requests.get(url = receive_median_occ_here)
                    spreadsheet_api_data = received_data.json()

                    if spreadsheet_api_data["status"] == 400:
                        print("Get median occupancy request error when last two dates were of different month")
                    
                    else:
                        api_arr = spreadsheet_api_data["data"]
                        _save_compute_two_(sheet, api_arr, med_occ)

                else:
                    print("condition error, where last two dates were from new month")
                
                print("Third condition executed")
                break

            elif str(todays_date_month).strip() == str(month_from_db).strip() and str(tomorrows_date_month).strip() == str(month_from_db).strip() and str(day_after_tomorrows_month).strip() != str(month_from_db).strip():
                
                if str(todays_date_month).strip() == str(month_from_db).strip() and str(tomorrows_date_month).strip() == str(month_from_db).strip():
                    _save_compute_three_(sheet, api_arr, med_occ)

                elif str(day_after_tomorrows_month).strip() != str(month_from_db).strip():

                    last_month = _get_last_month_()
                    _store_compute_(i, med_occ, last_month)

                    received_data = requests.get(url = receive_median_occ_here)
                    spreadsheet_api_data = received_data.json()

                    if spreadsheet_api_data["status"] == 400:
                        print("Get median occupancy request error")

                    else:
                        api_arr = spreadsheet_api_data["data"]
                        _save_compute_four_(sheet, api_arr, med_occ)

                else:
                    print("last date of different month case error")

                print("Fourth condition executed")
                break

            else:
                print("Error in month matching conditions")


if __name__== "__main__":
    main()

    price_list = []

    for (a, b, c) in zip(arbor_final_list, golf_final_list, cyber_final_list): 
        price_list.append(a)
        price_list.append(b)
        price_list.append(c)

    for item in price_list:
        send_perch_price_here = "https://api.nodal.direct/v1/index.php/Api/PerchDynamicPricePost"
        requests.post(url = send_perch_price_here, data = item)
    
    print("success")