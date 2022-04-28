"""
Write a Python program to find the date of the first Monday of a given week.
Sample Year and week : 2015, 50
Expected Output : Mon Dec 14 00:00:00 2015
"""
import datetime
print(datetime.datetime.strptime("2015 50 1", "%Y %W %w").ctime())
