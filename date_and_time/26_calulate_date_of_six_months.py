"""
Write a Python program calculates the date six months from the current date using the datetime module
"""
import datetime
d = datetime.date(2022, 8, 3)
add = 6
add = add + d.month
if add > 12:
    add = add-12
    add_date = datetime.date(d.year + 1, add, d.day)
    print((add_date - d).days, "days.")
else:
    add_date = datetime.date(d.year, add, d.day)
    print((add_date - d).days, 'days.')
