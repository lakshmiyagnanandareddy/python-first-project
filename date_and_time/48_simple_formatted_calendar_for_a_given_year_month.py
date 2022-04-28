"""
Write a Python program to display a simple, formatted calendar of a given year and month.
"""
import calendar
print("This is the program to print the calendar of month")
year = int(input("Enter year :"))
month = int(input("Enter month :"))
calendar.prmonth(theyear=year, themonth=month)
