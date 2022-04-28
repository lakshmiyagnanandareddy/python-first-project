"""
 Write a Python program to get a list of dates between two dates.
"""
import calendar
import datetime
from datetime import timedelta
d1 = datetime.date(2022, 3, 14)
d2 = datetime.date(2022, 5, 14)
for add in range((d2 - d1).days-1):
    print((d1 + timedelta(days=add+1)))
