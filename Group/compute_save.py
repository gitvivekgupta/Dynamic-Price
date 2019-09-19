import datetime
from compute_func import _forecast_data_, _forecast_data_one_, _forecast_data_two_, _forecast_data_three_, _forecast_data_four_

tomorrows_date = datetime.date.today() + datetime.timedelta(days=1)
tomorrows_date = tomorrows_date.strftime("%d-%b-%y")

day_after_tomorrows_date = datetime.date.today() + datetime.timedelta(days=2)
day_after_tomorrows_date = day_after_tomorrows_date.strftime("%d-%b-%y")

two_days_after_tomorrows_date = datetime.date.today() + datetime.timedelta(days=3)
two_days_after_tomorrows_date = two_days_after_tomorrows_date.strftime("%d-%b-%y")

def _save_compute_(i, api_arr, med_occ):

    for k in api_arr:
        arbor_suites_occ = k["arbor_suites_med_occ"]
        golf_course_occ = k["golf_course_med_occ"]
        cyber_city_occ = k["cyber_city_med_occ"]
    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_(i, med_occ, tomorrows_date, day_after_tomorrows_date, two_days_after_tomorrows_date)

    return 0

def _save_compute_one_(i, api_arr, med_occ):

    for k in api_arr:
        arbor_suites_occ = k["arbor_suites_med_occ"]
        golf_course_occ = k["golf_course_med_occ"]
        cyber_city_occ = k["cyber_city_med_occ"]
    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_one_(i, med_occ, tomorrows_date)

    return 0

def _save_compute_two_(i, api_arr, med_occ):

    for k in api_arr:
        arbor_suites_occ = k["arbor_suites_med_occ"]
        golf_course_occ = k["golf_course_med_occ"]
        cyber_city_occ = k["cyber_city_med_occ"]
    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_two_(i, med_occ, day_after_tomorrows_date, two_days_after_tomorrows_date)

    return 0

def _save_compute_three_(i, api_arr, med_occ):

    for k in api_arr:
        arbor_suites_occ = k["arbor_suites_med_occ"]
        golf_course_occ = k["golf_course_med_occ"]
        cyber_city_occ = k["cyber_city_med_occ"]
    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_three_(i, med_occ, tomorrows_date, day_after_tomorrows_date)

    return 0

def _save_compute_four_(i, api_arr, med_occ):

    for k in api_arr:
        arbor_suites_occ = k["arbor_suites_med_occ"]
        golf_course_occ = k["golf_course_med_occ"]
        cyber_city_occ = k["cyber_city_med_occ"]
    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_four_(i, med_occ, two_days_after_tomorrows_date)

    return 0