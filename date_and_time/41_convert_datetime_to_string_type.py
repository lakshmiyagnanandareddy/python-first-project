"""
Write a python program to generate a date and time as a string
"""
import datetime
d = datetime.datetime.now()
print(d.strftime("%H:%M %p\n%D"))
