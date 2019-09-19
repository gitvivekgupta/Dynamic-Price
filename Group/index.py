import json
import gspread
import datetime
import requests
from pprint import pprint
from get_median_occ import median_occupancy
from oauth2client.service_account import ServiceAccountCredentials
from compute_save import _save_compute_, _save_compute_one_, _save_compute_two_, _save_compute_three_, _save_compute_four_

tomorrows_date = datetime.date.today() + datetime.timedelta(days=1)
tomorrows_date = tomorrows_date.strftime("%d-%b-%y")

tomorrows_date_month = tomorrows_date[3: 6]
tomorrows_date_month = tomorrows_date_month.upper()

day_after_tomorrows_date = datetime.date.today() + datetime.timedelta(days=2)
day_after_tomorrows_date = day_after_tomorrows_date.strftime("%d-%b-%y")

day_after_tomorrows_month = day_after_tomorrows_date[3: 6]
day_after_tomorrows_month = day_after_tomorrows_month.upper()

two_days_after_tomorrows_date = datetime.date.today() + datetime.timedelta(days=3)
two_days_after_tomorrows_date = two_days_after_tomorrows_date.strftime("%d-%b-%y")

two_days_after_tomorrows_month = two_days_after_tomorrows_date[3: 6]
two_days_after_tomorrows_month = two_days_after_tomorrows_month.upper()

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

    post_data["month"] = tomorrows_date_month
    post_data["arbor_suites_med_occ"] = med_occ[0]
    post_data["golf_course_med_occ"] = med_occ[1]
    post_data["cyber_city_med_occ"] = med_occ[2]
    post_median_occ = json.dumps(post_data)

    send_median_occ_here = "https://api.nodal.direct/v1/index.php/Api/GroupDynamicPrice"
    requests.post(url = send_median_occ_here, data = post_median_occ)

    return 0

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

    for i in sheet:
        
        if spreadsheet_api_data["status"] == 400:
            print("Get median occupancy request error")

        else:

            api_arr = spreadsheet_api_data["data"]
            for j in api_arr:
                month_from_db = j["month"]

            if str(tomorrows_date_month).strip() == str(month_from_db).strip() and str(day_after_tomorrows_month).strip() == str(month_from_db).strip() and str(two_days_after_tomorrows_month).strip() == str(month_from_db).strip():
                _save_compute_(i, api_arr, med_occ)
                print("First condition executed")

            elif str(tomorrows_date_month).strip() != str(month_from_db).strip() and str(day_after_tomorrows_month).strip() != str(month_from_db).strip() and str(two_days_after_tomorrows_month).strip() != str(month_from_db).strip():
                last_month = _get_last_month_()
                _store_compute_(i, med_occ, last_month)
                _save_compute_(i, api_arr, med_occ)
                print("Second condition executed")

            elif str(tomorrows_date_month).strip() == str(month_from_db).strip() and str(day_after_tomorrows_month).strip() != str(month_from_db).strip() and str(two_days_after_tomorrows_month).strip() != str(month_from_db).strip():

                if str(tomorrows_date_month).strip() == str(month_from_db).strip():
                    _save_compute_one_(i, api_arr, med_occ)

                elif str(day_after_tomorrows_month).strip() != str(month_from_db).strip() and str(two_days_after_tomorrows_month).strip() != str(month_from_db).strip():

                    last_month = _get_last_month_()
                    _store_compute_(i, med_occ, last_month)

                    received_data = requests.get(url = receive_median_occ_here)
                    spreadsheet_api_data = received_data.json()

                    if spreadsheet_api_data["status"] == 400:
                        print("Get median occupancy request error")

                    else:
                        api_arr = spreadsheet_api_data["data"]
                        _save_compute_two_(i, api_arr, med_occ)

                    print("Third condition executed")

                else:
                    print("last date month check condition error")

            elif str(tomorrows_date_month).strip() == str(month_from_db).strip() and str(day_after_tomorrows_month).strip() == str(month_from_db).strip() and str(two_days_after_tomorrows_month).strip() != str(month_from_db).strip():

                if str(tomorrows_date_month).strip() == str(month_from_db).strip() and str(day_after_tomorrows_month).strip() == str(month_from_db).strip():
                    _save_compute_three_(i, api_arr, med_occ)

                elif str(two_days_after_tomorrows_month).strip() != str(month_from_db).strip():
                    
                    last_month = _get_last_month_()
                    _store_compute_(i, med_occ, last_month)

                    received_data = requests.get(url = receive_median_occ_here)
                    spreadsheet_api_data = received_data.json()

                    if spreadsheet_api_data["status"] == 400:
                        print("Get median occupancy request error")

                    else:
                        api_arr = spreadsheet_api_data["data"]
                        _save_compute_four_(i, api_arr, med_occ)

                else:
                    print("last two days month check condition error")

                print("Fourth condition executed")

            else:
                print("Error in month matching conditions")
                
    return 0

if __name__== "__main__":
    main()