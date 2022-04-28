"""
Write a Python program to get days between two dates.

Sample Dates : 2000,2,28, 2001,2,28
Expected Output : 366 days, 0:00:00
"""
import datetime
from datetime import date, timedelta
d1 = date(2000, 2, 28)
d2 = date(2001, 2, 28)
print(d2-d1)