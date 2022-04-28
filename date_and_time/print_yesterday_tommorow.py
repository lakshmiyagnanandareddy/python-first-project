# Write a Python program to convert the date to datetime (midnight of the date) in Python.
import datetime
from datetime import date
date = date.today()
print(date)
date_time = datetime.datetime(date.year, date.month, date.day)
print(date_time)