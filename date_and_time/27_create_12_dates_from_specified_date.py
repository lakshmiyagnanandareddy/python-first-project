"""
27. Write a Python program to create 12 fixed dates from a specified date over a given period.
The difference between two dates will be 20.
"""
import datetime
d = datetime.date(2020, 2, 23)
print("starting date :", d)
for _ in range(12):
    d = d + datetime.timedelta(days=20)
    print(d)