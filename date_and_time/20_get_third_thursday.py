"""
Write a Python program to test the third Tuesday of a month
"""
import datetime
d = datetime.date.today()
if d.weekday() == 1 and (22 > d.day > 14):
    print(True)
else:
    print(False)
print(d.weekday())
