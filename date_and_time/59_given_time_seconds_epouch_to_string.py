"""
Write a Python program to convert a given time in seconds since the epoch to a string representing local time.
Sample Output:
Tue Apr 13 11:51:51 2021
Thu Jun 30 18:36:29 1977
"""
import calendar
import time
d1 = calendar.timegm(time.strptime("Tue Apr 13 11:51:51 2021", "%a %b %d %H:%M:%S %Y"))
print("Tue Apr 13 11:51:51 2021, in epoch seconds :", d1)
d2 = calendar.timegm(time.strptime("Thu Jun 30 18:36:29 1977", "%a %b %d %H:%M:%S %Y"))
print("Thu Jun 30 18:36:29 1977, in epoch seconds :", d2)
