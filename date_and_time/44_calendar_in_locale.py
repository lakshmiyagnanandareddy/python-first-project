"""
Write a Python program to display a calendar for a locale
"""
import calendar
locale = calendar.LocaleTextCalendar(locale=en_IN.utf8)
print(locale.prmonth(theyear=2022, themonth=3))
