"""
Write a Python program to print simple format of time,
full names and the representation format and preferred date time format.
Simple format of time:
Tue, 13 Apr 2021 12:02:01 + 1010
Full names and the representation:
Tuesday, 04/13/21 April 2021 12:02:01 + 0000
Preferred date time format:
Tue Apr 13 12:02:01 2021
Example 11: 04/13/21, 12:02:01, 21, 2021
"""
import time
from time import gmtime
print("Simple format of time:")
print(time.strftime("%a, %d %b %Y %H:%M:%S %z + 1010", gmtime()))
print("full names and the representation :")
print(time.strftime("%A, %D %B %Y %H:%M:%S + 0000", gmtime()))
print("Preferred date time format :")
print(time.ctime())
