"""
 Write a Python program to calculate two date difference in seconds
"""
import datetime
import time
d1 = datetime.date(2022, 3, 4)
d2 = datetime.date(2022, 8, 2)
difference_in_seconds = (d2-d1).total_seconds()
print(difference_in_seconds)

