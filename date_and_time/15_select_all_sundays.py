"""
Write a Python program to select all the Sundays of a specified year
"""
import datetime
from datetime import date,timedelta
year = int(input("Enter the year : "))

d = date(year, 1, 1)
d += timedelta(days=6 - d.weekday())
while year == d.year:
    print(d)
    d += timedelta(days=7)




