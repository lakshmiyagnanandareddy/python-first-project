"""
Write a Python program to convert a string into datetime
"""
import datetime
print(datetime.datetime.strptime("Jan 03 2022 03 30 22 am", "%b %d %Y %I %M %S %p"))