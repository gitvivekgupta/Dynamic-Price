from compute_func import _forecast_data_, _forecast_data_one_, _forecast_data_two_, _forecast_data_three_, _forecast_data_four_

def _save_compute_(sheet, api_arr, med_occ):

    arbor_suites_occ = api_arr["arbor_suites_med_occ"]
    golf_course_occ = api_arr["golf_course_med_occ"]
    cyber_city_occ = api_arr["cyber_city_med_occ"]
        
    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_(sheet, med_occ)

def _save_compute_one_(sheet, api_arr, med_occ):

    arbor_suites_occ = api_arr["arbor_suites_med_occ"]
    golf_course_occ = api_arr["golf_course_med_occ"]
    cyber_city_occ = api_arr["cyber_city_med_occ"]
        
    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_one_(sheet, med_occ)

def _save_compute_two_(sheet, api_arr, med_occ):

    arbor_suites_occ = api_arr["arbor_suites_med_occ"]
    golf_course_occ = api_arr["golf_course_med_occ"]
    cyber_city_occ = api_arr["cyber_city_med_occ"]

    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_two_(sheet, med_occ)

def _save_compute_three_(sheet, api_arr, med_occ):

    arbor_suites_occ = api_arr["arbor_suites_med_occ"]
    golf_course_occ = api_arr["golf_course_med_occ"]
    cyber_city_occ = api_arr["cyber_city_med_occ"]

    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_three_(sheet, med_occ)

def _save_compute_four_(sheet, api_arr, med_occ):

    arbor_suites_occ = api_arr["arbor_suites_med_occ"]
    golf_course_occ = api_arr["golf_course_med_occ"]
    cyber_city_occ = api_arr["cyber_city_med_occ"]

    med_occ.append(arbor_suites_occ)
    med_occ.append(golf_course_occ)
    med_occ.append(cyber_city_occ)

    _forecast_data_four_(sheet, med_occ)