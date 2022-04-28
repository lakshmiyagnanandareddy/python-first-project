"""
Write a Python program to get the date of the last Tuesday.
"""
import datetime
from datetime import date, timedelta
d = datetime.date(2022, 4, 21)
dat = datetime.timedelta(days=(7 + d.isoweekday()-2))
print(d-dat)
print((d-dat).strftime("%A"))