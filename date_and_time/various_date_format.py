import datetime
from datetime import date
print("Current date and time :", datetime.datetime.now())
print("year :", datetime.datetime.now().year)
print("Month : ", date.today().month)
print("Week number of year :", date.today().isocalendar().week)
print("Day of year :", date.today().timetuple().tm_yday)
print("Day of month :", date.today().day)
print("Day of week :", date.today().weekday())