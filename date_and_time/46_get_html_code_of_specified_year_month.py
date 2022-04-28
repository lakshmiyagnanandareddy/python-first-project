"""
Write a Python program to create a HTML calendar with data for a specific year and month.
"""
import calendar
HTML_of_year = calendar.HTMLCalendar().formatmonth(theyear=2022, themonth=4, withyear=True)
print(HTML_of_year)