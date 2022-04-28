import datetime
number_of_mondays = 0
for months in range(12):
     d = datetime.date(2015, months+1, 1)
    if d.day == d.isoweekday():
        number_of_mondays = number_of_mondays+1
print(number_of_mondays)
