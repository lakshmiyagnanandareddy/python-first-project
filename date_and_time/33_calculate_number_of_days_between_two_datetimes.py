"""
Write a Python program to calculate no of days between two datetime.
"""
import datetime
d1 = datetime.datetime(2022, 2, 6, 2)
d2 = datetime.datetime(2023, 3, 5, 6)
number_days_between_two_days = d2 - d1
print(number_days_between_two_days.days)