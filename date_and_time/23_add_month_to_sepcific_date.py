"""
Write a Python program to add a month with a specified date.
"""
import calendar
import datetime
d = datetime.date(2022, 4, 23)
number_of_days = calendar.monthrange(2022, 4)[1]
print(number_of_days)
print(d+datetime.timedelta(days=number_of_days))