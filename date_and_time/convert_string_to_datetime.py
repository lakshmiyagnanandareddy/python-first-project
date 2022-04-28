import datetime
year = "Jan 1 2014 2:43 pm"
print(year)
print(type(year))
year_conversion = datetime.datetime.strptime(year, "%b %d %Y %I:%M %p")
print(year_conversion)
print(type(year_conversion))