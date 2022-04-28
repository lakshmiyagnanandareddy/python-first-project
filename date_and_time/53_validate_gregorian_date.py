"""
Write a Python program to validate a Gregorian date.
The month is between 1 and 12 inclusive, the day is within the allowed number of days for the given month.
Leap year's are taken into consideration.
The year is between 1 and 32767 inclusive
"""
import datetime
import calendar
def check(d, m, y):
    if y <= 32767:
        try:
            datetime.date(y, m, d)
            return True
        except ValueError:
            return False
    else:
        return False

print(check(20, 2, 293744))
