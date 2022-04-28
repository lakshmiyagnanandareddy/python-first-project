"""
Write a Python program to drop microseconds from datetime.
"""
import datetime
d = datetime.datetime(2022, 4, 20, 23, 25, 57, 62245)
d = d.replace(microsecond=00000)
print(d)