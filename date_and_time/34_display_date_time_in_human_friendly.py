"""
 Write a Python program to display the date and time in a human-friendly string.
"""
from datetime import date
import datetime
d1 = datetime.datetime(2022, 2, 3, 4).strftime("%B %d, %Y %I:%M:%S %p")
print(d1)