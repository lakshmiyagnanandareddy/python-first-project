"""
Write a Python program to get week number.

Sample Date : 2015, 6, 16
Expected Output : 25
"""
import datetime
print(datetime.date(2015, 6, 16).isocalendar().week)