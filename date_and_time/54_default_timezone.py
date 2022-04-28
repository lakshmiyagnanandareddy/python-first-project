"""
Write a Python program to set the default timezone used by all date/time functions
"""
import calendar
import datetime
d = datetime.datetime.now(tz=None)
print(d)
print(d.tzinfo)

