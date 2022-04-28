"""
Write a Python program to calculate a number of days between two dates.
"""
from datetime import date
d1 = date(2022, 2, 2)
d2 = date(2022, 4, 5)
number_of_days_between_these_days = d2 - d1
print(number_of_days_between_these_days.days)
