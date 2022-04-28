"""
Write a Python program to get the first and last second.
"""
import datetime
print("first second :", str(datetime.time.min)[6:8])
print("last second :", str(datetime.time.max)[6:8])