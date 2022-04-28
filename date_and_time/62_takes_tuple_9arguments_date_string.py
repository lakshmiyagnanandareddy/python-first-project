"""
Write a Python program that takes a tuple containing 9 elements corresponding to structure time as an argument
and returns a string representing it.

Result: Sun Jan 22 02:34:06 2020
Result: Tue Nov 12 02:54:08 1982
"""
import time
import calendar
# t = calendar.timegm()
t = time.strptime("Tue Apr 13 2021 11:51:51", "%a %b %d %Y %H:%M:%S")
print("Result :", time.asctime(t))
