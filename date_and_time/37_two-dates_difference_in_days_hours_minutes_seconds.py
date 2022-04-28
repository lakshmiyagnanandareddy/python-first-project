"""
Write a Python program to convert two date difference in days, hours, minutes, seconds.
"""
import datetime
d1 = datetime.date(2022, 4, 5)
d2 = datetime.date(2022, 6, 9)
difference_in_days = (d2 - d1).days
difference_in_hours = (d2 - d1).days * 24
difference_in_minutes = (d2 - d1).days * 24 * 60
difference_in_seconds = (d2 - d1).total_seconds()
print("difference in days :", difference_in_days)
print("difference in hours :", difference_in_hours)
print("difference in minutes :", difference_in_minutes)
print("difference in seconds :", int(difference_in_seconds))

