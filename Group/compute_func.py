import re

from arbor_property import _perch_arbor_suites_
from golf_property import _golf_course_
from cyber_property import _cyber_city_
from dates import todays_date, todays_date_month, tomorrows_date, tomorrows_date_month
from dates import day_after_tomorrows_date, day_after_tomorrows_month

def surge_index(percentage):

        percentage = float(percentage)

        if percentage > 80:
                surge_index = 50

        elif percentage > 60 and percentage <= 80:
                surge_index = 60

        else:
                surge_index = 80

        return float(surge_index)

def _forecast_(i, j, med_occ, forecast_date):

        arbor_surge_index = surge_index(med_occ[0])
        golf_surge_index = surge_index(med_occ[1])
        cyber_surge_index = surge_index(med_occ[2])

        _perch_arbor_suites_(i, j, arbor_surge_index, forecast_date)
        _golf_course_(i, j, golf_surge_index, forecast_date)
        _cyber_city_(i, j, cyber_surge_index, forecast_date)

def _second_next_day_forecast_(i, j, med_occ, date):
        _forecast_(i, j, med_occ, date)

def _next_day_forecast_(i, j, med_occ, date):
        _forecast_(i, j, med_occ, date)
        
def _forecast_data_(sheet, med_occ):

        for i in sheet:

                i_str = str(i)
                sheet_month = re.findall(r"'(.*?)'", i_str)
                sheet_month = sheet_month[0]
                sheet_month = sheet_month[:3]

                if str(sheet_month).strip() == str(todays_date_month).strip() and str(sheet_month).strip() == str(tomorrows_date_month).strip() and str(sheet_month).strip() == str(day_after_tomorrows_month).strip(): 

                        for j in range(4, 35):

                                sheet_date = i.cell(j, 1)
                                sheet_date = str(sheet_date)
                                sheet_date = re.findall(r"'(.*?)'", sheet_date)
                                sheet_date = sheet_date[0]

                                if str(sheet_date).strip() == str(todays_date).strip():
                                
                                        _forecast_(i, j, med_occ, todays_date)
                                        _next_day_forecast_(i, j+1, med_occ, tomorrows_date)
                                        _second_next_day_forecast_(i, j+2, med_occ, day_after_tomorrows_date)
                                        break
                                
                                # else:
                                #         print("function _forecast_data_ error")
                                #         pass
                else:
                        pass

def _forecast_data_one_(sheet, med_occ):

        for i in sheet:

                i_str = str(i)
                sheet_month = re.findall(r"'(.*?)'", i_str)
                sheet_month = sheet_month[0]
                sheet_month = sheet_month[:3]

                if str(sheet_month).strip() == str(todays_date_month).strip():
                        
                        for j in range(4, 35):

                                sheet_date = i.cell(j, 1)
                                sheet_date = str(sheet_date)
                                sheet_date = re.findall(r"'(.*?)'", sheet_date)
                                sheet_date = sheet_date[0]

                                if str(sheet_date).strip() == str(todays_date).strip():

                                        _forecast_(i, j, med_occ, todays_date)
                                        break
                                
                                # else:
                                #         print("function _forecast_data_one_ error")
                                #         pass
                else:
                        pass

def _forecast_data_two_(sheet, med_occ):

        for i in sheet:

                i_str = str(i)
                sheet_month = re.findall(r"'(.*?)'", i_str)
                sheet_month = sheet_month[0]
                sheet_month = sheet_month[:3]

                if str(sheet_month).strip() == str(tomorrows_date_month).strip() and str(sheet_month).strip() == str(day_after_tomorrows_month).strip():
                        
                        for j in range(4, 35):

                                sheet_date = i.cell(j, 1)
                                sheet_date = str(sheet_date)
                                sheet_date = re.findall(r"'(.*?)'", sheet_date)
                                sheet_date = sheet_date[0]

                                if str(sheet_date).strip() == str(tomorrows_date).strip():
                                
                                        _next_day_forecast_(i, j+1, med_occ, tomorrows_date)
                                        _second_next_day_forecast_(i, j+2, med_occ, day_after_tomorrows_date)
                                        break
                                
                                # else:
                                #         print("function forecast_data_two error error")
                                #         pass
                else:
                        pass

def _forecast_data_three_(sheet, med_occ):

        for i in sheet:

                i_str = str(i)
                sheet_month = re.findall(r"'(.*?)'", i_str)
                sheet_month = sheet_month[0]
                sheet_month = sheet_month[:3]

                if str(sheet_month).strip() == str(tomorrows_date_month) and str(sheet_month).strip() == str(day_after_tomorrows_month):
                        
                        for j in range(4, 35):

                                sheet_date = i.cell(j, 1)
                                sheet_date = str(sheet_date)
                                sheet_date = re.findall(r"'(.*?)'", sheet_date)
                                sheet_date = sheet_date[0]

                                if str(sheet_date).strip() == str(todays_date).strip():
                                
                                        _forecast_(i, j, med_occ, todays_date)
                                        _next_day_forecast_(i, j+1, med_occ, tomorrows_date)
                                        break
                                
                                # else:
                                #         print("function _forecast_data_three_ error")
                                #         pass
                else:
                        pass

def _forecast_data_four_(sheet, med_occ):

        for i in sheet:

                i_str = str(i)
                sheet_month = re.findall(r"'(.*?)'", i_str)
                sheet_month = sheet_month[0]
                sheet_month = sheet_month[:3]

                if str(sheet_month).strip() == str(tomorrows_date_month) and str(sheet_month).strip() == str(day_after_tomorrows_month):
                        
                        for j in range(4, 35):

                                sheet_date = i.cell(j, 1)
                                sheet_date = str(sheet_date)
                                sheet_date = re.findall(r"'(.*?)'", sheet_date)
                                sheet_date = sheet_date[0]

                                if str(sheet_date).strip() == str(day_after_tomorrows_date).strip():
                                
                                        _second_next_day_forecast_(i, j+2, med_occ, day_after_tomorrows_date)
                                        break
                                
                                # else:
                                #         print("function _forecast_data_four_ error")
                                #         pass
                else:
                        pass