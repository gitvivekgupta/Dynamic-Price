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
arbor_list = []
golf_list = []
cyber_list = []

def median_occupancy(i, last_month):
        
        for i in sheet:

                current_sheet = str(i)
                found = current_sheet.find(str(last_month))

                if found == -1:

                        arbor_current_occ = i.cell(37, 5).value
                        arbor_current_occ = arbor_current_occ[:4]

                        golf_current_occ = i.cell(37, 11).value
                        golf_current_occ = golf_current_occ[:4]

                        cyber_current_occ = i.cell(37, 17).value
                        cyber_current_occ = cyber_current_occ[:4]

                        arbor_list.append(float(arbor_current_occ))
                        golf_list.append(float(golf_current_occ))                      
                        cyber_list.append(float(cyber_current_occ))

                        time.sleep(70)

                else:
                        print("Compute successfull till", i)
                        break
                        

        arbor_median = statistics.median(arbor_list)
        golf_median = statistics.median(golf_list)
        cyber_median = statistics.median(cyber_list)

        medians.append(arbor_median)
        medians.append(golf_median)
        medians.append(cyber_median)

        return medians