"""
Write a Python program to get the number of days of a given month and year.
"""
import calendar
import datetime
day = datetime.date(2022, 2, 1)
maximum_days = calendar.monthrange(day.year, day.month)
print("the number of days of the", day.month, "is", maximum_days[1])
