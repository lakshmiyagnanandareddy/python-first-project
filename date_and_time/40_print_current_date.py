"""
Write a Python program to get the current date time information.
"""
import datetime
d = datetime.datetime.now()
print(d.strftime("%H:%M %p\n%D"))