"""
Write a Python program to add 5 seconds with the current time.
Sample Data :
13:28:32.953088
13:28:37.953088
"""
from datetime import time
import datetime
current_time = datetime.datetime.today()
print(type(current_time))
print(current_time)
adding_5_days = datetime.timedelta(seconds=5)
print(current_time+adding_5_days)