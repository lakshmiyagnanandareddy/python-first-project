"""
 Write a Python program to display formatted text output of a month and start weeks on Sunday
"""
import calendar
calendar.TextCalendar(firstweekday=6).prmonth(theyear=2022, themonth=4)