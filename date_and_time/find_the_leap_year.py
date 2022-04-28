import datetime
from datetime import date

print("The program is to check weather th year is the leap year or not!!")
yea = int(input("Enter the year : "))

try:
    d = date(yea, 2, 29).strftime("%Y %b %d")
    year = datetime.datetime.strptime(d, '%Y %b %d')
    print(year.year, "Is the leap year.")

except:
    print(yea, "This is not a leap year.")
