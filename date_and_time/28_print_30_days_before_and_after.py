"""
Write a Python program to get the dates 30 days before and after from the current date
"""
import datetime
d = datetime.date(2022, 3, 23)
print(d - datetime.timedelta(days=30))
print(d + datetime.timedelta(days=30))

