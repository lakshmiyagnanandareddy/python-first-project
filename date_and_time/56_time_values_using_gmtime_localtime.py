"""
Write a Python program to get time values with components using local time and gmtime.
"""
import time
import datetime
import calendar

print(time.gmtime(time.time()))
print(time.localtime(time.time()))