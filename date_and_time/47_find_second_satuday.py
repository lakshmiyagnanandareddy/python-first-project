"""
Write a Python program display a list of the dates for the 2nd Saturday of every month for a given year.
"""
import datetime
import calendar
year = 2022
for month in range(12):
    week = calendar.monthcalendar(year, month+1)
    first_week = week[0]
    second_week = week[1]
    third_week = week[2]
    if first_week[calendar.SATURDAY]:
        print("month :", datetime.date(year, month+1, 1).strftime("%B"), ",date of second saturday :", second_week[calendar.SATURDAY])
    else:
        print("month :", datetime.date(year, month+1, 1).strftime("%B"), ",date of second saturday :", third_week[calendar.SATURDAY])
