import datetime

todays_date = datetime.date.today() + datetime.timedelta(days=0)
todays_date = todays_date.strftime("%d-%b-%y")

todays_date_month = todays_date[3: 6]
todays_date_month = todays_date_month.upper()

tomorrows_date = datetime.date.today() + datetime.timedelta(days=1)
tomorrows_date = tomorrows_date.strftime("%d-%b-%y")

tomorrows_date_month = tomorrows_date[3: 6]
tomorrows_date_month = tomorrows_date_month.upper()

day_after_tomorrows_date = datetime.date.today() + datetime.timedelta(days=2)
day_after_tomorrows_date = day_after_tomorrows_date.strftime("%d-%b-%y")

day_after_tomorrows_month = day_after_tomorrows_date[3: 6]
day_after_tomorrows_month = day_after_tomorrows_month.upper()
