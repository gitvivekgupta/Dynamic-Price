import time
import gspread
import statistics

from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import date

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)
sheet = client.open("(2019) GROUP OCCUPANCY")

medians = []
prop_one_list = []
prop_two_list = []
prop_three_list = []

def median_occupancy(i, last_month):
        
        for i in sheet:

                current_sheet = str(i)
                found = current_sheet.find(str(last_month))

                if found == -1:

                        one_week_one = i.cell(10, 6).value
                        one_week_one = one_week_one[:5]

                        one_week_two = i.cell(17, 6).value
                        one_week_two = one_week_two[:5]

                        one_week_three = i.cell(24, 6).value
                        one_week_three = one_week_three[:5]

                        one_week_four = i.cell(33, 6).value
                        one_week_four = one_week_four[:5]

                        two_week_one = i.cell(10, 12).value
                        two_week_one = two_week_one[:5]

                        two_week_two = i.cell(17, 12).value
                        two_week_two = two_week_two[:5]

                        two_week_three = i.cell(24, 12).value
                        two_week_three = two_week_three[:5]

                        two_week_four = i.cell(33, 12).value
                        two_week_four = two_week_four[:5]

                        three_week_one = i.cell(10, 18).value
                        three_week_one = three_week_one[:5]

                        three_week_two = i.cell(17, 18).value
                        three_week_two = three_week_two[:5]

                        three_week_three = i.cell(24, 18).value
                        three_week_three = three_week_three[:5]

                        three_week_four = i.cell(33, 18).value
                        three_week_four = three_week_four[:5]

                        prop_one_list.append(float(one_week_one))
                        prop_one_list.append(float(one_week_two))
                        prop_one_list.append(float(one_week_three))
                        prop_one_list.append(float(one_week_four))

                        prop_two_list.append(float(two_week_one))
                        prop_two_list.append(float(two_week_two))
                        prop_two_list.append(float(two_week_three))
                        prop_two_list.append(float(two_week_four))

                        prop_three_list.append(float(three_week_one))
                        prop_three_list.append(float(three_week_two))
                        prop_three_list.append(float(three_week_three))
                        prop_three_list.append(float(three_week_four))

                        time.sleep(100)

                else:
                        print("Last month not found in google sheets", i)
                        

        prop_one_median = statistics.median(prop_one_list)
        prop_two_median = statistics.median(prop_two_list)
        prop_three_median = statistics.median(prop_three_list)

        medians.append(prop_one_median)
        medians.append(prop_two_median)
        medians.append(prop_three_median)

        return medians