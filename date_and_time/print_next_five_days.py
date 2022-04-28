# Write a Python program to print next 5 days starting from today.
from datetime import date
import datetime
for next_day in range(5):
    next_d = datetime.timedelta(days=next_day+1)
    print((date.today()+next_d).strftime("%A"))
