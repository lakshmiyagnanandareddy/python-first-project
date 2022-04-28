"""
Write a Python program to get the current week
"""
import datetime
d = datetime.date(2022, 4, 6)
print("current week of date", d.strftime("%W"))
