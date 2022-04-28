"""
 Write a Python program to get the GMT and local current time.
"""
import datetime
import time
from time import strftime, gmtime
print(time.strftime("%a, %d %Y %I: %M: %S %p %Z", time.gmtime()))
print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))
