import datetime
from base_price import arbor_base_price, golf_base_price, cyber_base_price
from arbor_property import _perch_arbor_suites_
from golf_property import _golf_course_
from cyber_property import _cyber_city_

def surge_index(percentage):

        if percentage > 80:
                surge_index = 50
        elif percentage > 60 and percentage <= 80:
                surge_index = 60
        else:
                surge_index = 80

        return surge_index

def _forecast_(i, j, med_occ):

        arbor_data_dict = {}
        golf_data_dict = {}
        cyber_data_dict = {}

        arbor_surge_index = surge_index(med_occ[0])
        golf_surge_index = surge_index(med_occ[1])
        cyber_surge_index = surge_index(med_occ[2])

        _perch_arbor_suites_(i, j, arbor_surge_index, arbor_data_dict)
        _golf_course_(i, j, golf_surge_index, golf_data_dict)
        _cyber_city_(i, j, cyber_surge_index, cyber_data_dict)

        return 0

def _forecast_data_(i, med_occ, tomorrows_date, day_after_tomorrows_date, two_days_after_tomorrows_date):

        for j in range(4, 35):
                
                sheet_date = i.cell(j, 1)

                if str(sheet_date).strip() == str(tomorrows_date).strip():
                        _forecast_(i, j, med_occ)

                elif str(sheet_date).strip() == str(day_after_tomorrows_date).strip():
                        _forecast_(i, j, med_occ)

                elif str(sheet_date).strip() == str(two_days_after_tomorrows_date).strip():
                        _forecast_(i, j, med_occ)
                
                else:
                        print("can't match sheet date with forecast dates - case all same")
                        pass

        return 0

def _forecast_data_one_(i, med_occ, tomorrows_date):

        for j in range(4, 35):

                sheet_date = i.cell(j, 1)

                if str(sheet_date).strip() == str(tomorrows_date).strip():
                        _forecast_(i, j, med_occ)
                
                else:
                        print("can't match sheet date with forecast dates - case last two different")
                        pass

        return 0

def _forecast_data_two_(i, med_occ, day_after_tomorrows_date, two_days_after_tomorrows_date):

        for j in range(4, 35):

                sheet_date = i.cell(j, 1)

                if str(sheet_date).strip() == str(day_after_tomorrows_date).strip():
                        _forecast_(i, j, med_occ)

                elif str(sheet_date).strip() == str(two_days_after_tomorrows_date).strip():
                        _forecast_(i, j, med_occ)
                
                else:
                        print("can't match sheet date with forecast dates - case last two different")
                        pass

        return 0

def _forecast_data_three_(i, med_occ, tomorrows_date, day_after_tomorrows_date):

        for j in range(4, 35):

                sheet_date = i.cell(j, 1)

                if str(sheet_date).strip() == str(tomorrows_date).strip():
                        _forecast_(i, j, med_occ)

                elif str(sheet_date).strip() == str(day_after_tomorrows_date).strip():
                        _forecast_(i, j, med_occ)
                
                else:
                        print("can't match sheet date with forecast dates - case last different")
                        pass

        return 0

def _forecast_data_four_(i, med_occ, two_days_after_tomorrows_date):

        for j in range(4, 35):

                sheet_date = i.cell(j, 1)

                if str(sheet_date).strip() == str(two_days_after_tomorrows_date).strip():
                        _forecast_(i, j, med_occ)
                
                else:
                        print("can't match sheet date with forecast dates - case last different")
                        pass

        return 0