"""
Write a Python program to add year(s) with a given date and display the new date.
Sample Data : (addYears is the user defined function name)
print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))

Expected Output :
2014-01-01
2015-01-01
2017-01-01
2001-03-01
"""
import datetime
from datetime import date
"""
date_year = int(input("Enter year : "))
date_month = int(input("Enter month : "))
date_date = int(input("Enter date : "))

current_time = date(date_year, date_month, date_date)
print(current_time)
add_years = int(input("Enter years you want to add : "))

addition_years = date(current_time.year+add_years, current_time.month, current_time.day)
updated_year = datetime.datetime.strptime(str(addition_years.year), "%Y")
print(updated_year)
"""


def addYears(d, years):
    try:
        return date(d.year+years, d.month, d.day)
    except:
        return d+(date(d.year+years, 1, 1) - date(d.year, 1, 1))


print(addYears(datetime.date(2015, 1, 1), -1))
print(addYears(datetime.date(2015, 1, 1), 0))
print(addYears(datetime.date(2015, 1, 1), 2))
print(addYears(datetime.date(2000, 2, 29), 1))
