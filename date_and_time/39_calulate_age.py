"""
Write a Python program to calculate an age in year.
"""
from datetime import date
date_of_birth = date(2002, 6, 7)
age_in_days = (date.today().year - date_of_birth.year - ((date.today().month, date.today().day) < (date_of_birth.month, date_of_birth.day)))
print(age_in_days)
print()
