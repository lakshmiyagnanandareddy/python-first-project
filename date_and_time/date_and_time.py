import datetime
import pytz


print(datetime.datetime.now().date())   # .date() will give date.

print(datetime.datetime.now().time())   # .time() will give time.

print(datetime.datetime(202, 4, 14))
print(datetime.datetime)
print(datetime.MINYEAR)     # .MINYEAR - will give the smallest year present in the datetime object.

print(datetime.MAXYEAR)     # .MAXYEAR - will give the biggest year present in the datetime object.

print("Strftime of shortform of year :", datetime.datetime.now().strftime("%y"))   # strftime("%y") - will give year in short.
print("Strftime of fullform of year :", datetime.datetime.now().strftime("%Y"))   # strftime("%Y") - will give year in full form.
print("Strftime of shortform of month :", datetime.datetime.now().strftime("%b"))   # strftime("%b") - will give month in the short form.
print("Strftime of fullform of month :", datetime.datetime.now().strftime("%B"))   # strftime("%B") - will give month in the full form.
print("Strftime of shortform of day :", datetime.datetime.now().strftime("%a"))     # strftime("%a") - will give day in the short form.
print("Strftime of full form of day :", datetime.datetime.now().strftime("%A"))     # strftime("%A") - will give day in the full form.
print("strftime of will give time in 24hours format ;", datetime.datetime.now().strftime("%H"))     # strftime("%H") - will give time in 24hours format.
print("Strftime will give 12 hours format :", datetime.datetime.now().strftime("%I"))   # strftime("%I") - will give time in 12 hours format.
print("Strftime will give am/pm :", datetime.datetime.now().strftime("%p"))     # strftime(%P) - will give time in am/pm format.
print("strftime of minutes in time :", datetime.datetime.now().strftime("%M"))   # strftime(%M) - will give minutes.
print("strftime of seconds in time :", datetime.datetime.now().strftime("%S"))  # strftime(%S) - will give seconds.
print("strftime of microseconds in time :", datetime.datetime.now().strftime("%f")) # strftime(%F) - will give milliseconds.

strtime = "june 20 2022"
print("strptime of dates format is :", datetime.datetime.strptime(strtime, "%B %d %Y")) # will comvert normal date time to dateime format
# it means will convert string date format to datetime format.

d = datetime.date(2022, 2, 24)
print(d)
todayDate = datetime.date.today()  # today() - will give today date format.
print(todayDate)

todayDateDay = datetime.date.today().day    # today().day - will give date of today.
print(todayDateDay)

todayDateMonth = datetime.date.today().month    # today().month - will give month of today.
print(todayDateMonth)

todayDateYear = datetime.date.today().year  # today().year - will give year of today.
print(todayDateYear)

weekDay = datetime.date.today().weekday()   # today().weekday() - will give week day in 0-6 days in a week.
print(weekDay)

weeKDay = datetime.date.today().isoweekday()    # today().isoweekday() - will give week day in 1-7 days in a week.
print(weeKDay)

tdelta = datetime.timedelta(22)     # timedelta() - is used to (add or increase) or (sub (or) decrease) the (days, seconds, hours, minutes, weeks).
print(todayDate + tdelta)

birthDay = datetime.date(2022, 6, 7)
print(birthDay - todayDate)

tDay = datetime.datetime.today()
now = datetime.datetime.now()
utcnow = datetime.datetime.utcnow()
# today() - will give today datetime format.
# now() - will give today datetime format ,the difference is we can give timezone in this.
# utcnow() - will give today datetime format, but in the utc format.
print("today() :", tDay)
print("now() :", now)
print("utcnow : ", utcnow)

print("pytz :", datetime.datetime.now(tz=pytz.UTC))
print("pytz timezone :", datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone("US/Mountain")))
# we will get time as for time zone.

from datetime import date
d = date(2022, 3, 12)
print(d)

print("from date : ", date.today())

import time
import datetime
d = time.time()
print(d)
dt = datetime.datetime.now().time()
print(dt)
print("timestamp d :", datetime.date.fromtimestamp(d))  # it will give the date from the time.
# print("timestamp dt :", datetime.datetime.fromtimestamp(dt))
print("from ordinal :", datetime.date.fromordinal(165028))
d_isoformat = date.fromisoformat("2022-04-12")   # it will convert normal string to date.
print(type(d_isoformat))
print("form iso format : ", d_isoformat.day)

print("form iso calender :", date.fromisocalendar(2022, 24, 5))     # fromisocalender(year, month, day) - will give the date from taking the arguments
# year - integertype.
# month - 52 weeks.
# days - range[1-7].
datelist = [2022-2-21, 2021-2-1, 2111-5-22, 1999-3-22]
print("MIN date :", date(2022, 2, 22).min)

print("resolution :", )

print("")



print("calender :")



import calendar
de = calendar.Calendar(firstweekday=0)  # it will take the calender from that week.
for d in de.iterweekdays():     # it will give week days sarting with firstweekoftheday.
    print("iter week days :", d)

for d in de.itermonthdates(year=2022, month=2): # it will give the dates of the particular given month and starting with given firstweekday.
    print("iter month dates :", d)

for d in de.itermonthdays(year=2022, month=2):  # it will give the days of the particular given days of the particular given year,month and starting with given firstweekday and outside of that month will remain "0".
    print("iter month days ;", d)

for d in de.itermonthdays2(year=2022, month=2):  # it will give the (days, weekday) of the particular given days of the particular given year,month and starting with given firstweekday.
    print("itermonthdays2 :", d)

for d in de.itermonthdays3(year=2022, month=2):  # it will give the (year, month, days) of the particular given days of the particular given year,month and starting with given firstweekday.
    print("iter month days 3 :", d)

for d in de.itermonthdays4(year=2022, month= 2):    # it will give the (year, month, days, weekday) of the particular given days of the particuar given year,month and starting with given firstweekday.
    print("iter month days 4", d)

for d in de.monthdatescalendar(year=2022, month=2):  # it will give the date of weeks in one lists.
    print("months dates calender :", d)

for d in de.monthdayscalendar(year=2022, month=2):  # it will gives the weekdays of a weeks in lists
    print("month days calender :", d)

for d in de.monthdays2calendar(year=2022, month=2):   # it will gives the (day number, week number) of weeks in lists.
    print("month days2 calender :", d)

for d in de.yeardatescalendar(year=2022, width=12):     # it will give that many width = months in a rows of list.
    print("year dates calender :", d)

for d in de.yeardays2calendar(year=2022, width=5):  # it will give that many width = months in a row with tuple(date, weekday)in the list.
    print("yeardays2calender :", d)

print("year days calender :", de.yeardayscalendar(year=2022, width=12))  # it will give the calender with dates of a spwcified.


print("calennder.textcalender :")

calender_textcalender = calendar.TextCalendar(firstweekday=0).formatmonth(theyear=2022, themonth=2, w=2, l=3)   # here it will gives calender of specified month and seperated with the help of w and l.
print('calender_textcalender :', calender_textcalender)

calendar.TextCalendar().prmonth(theyear=2022, themonth=5, w=2, l=1)  # it will give the calendar of the specified month
# print("calender_prmonth :", calendar.TextCalendar(firstweekday=0).prmonth(theyear=2022, themonth=2, w=2, l=1))

print("format year", calendar.TextCalendar().formatyear(theyear=2022, w=2, l=2, c=3, m=2))  # it will give the year of the specified year.

print("pryear :")
calendar.TextCalendar().pryear(theyear=2022)

print("calender_HTMLCalendar :")
print("calender_HtMLCalendar_formatmonth :\n", calendar.HTMLCalendar().formatmonth(theyear=2022, themonth=2, withyear=True))  # it will give the calendar in the html format with given specified year, month and withyear(True/False - it will give the year if we want on the header.)

print("calender_HTMLCalendar_formatyear :\n", calendar.HTMLCalendar().formatyear(theyear=2022, width=3))

print("calender_HTMLCalender_formatyearpage :\n", calendar.HTMLCalendar().formatyearpage(theyear=2022, width=3, css="calendar.css", encoding=None))  # it will give the calendar of the specified year, we can give css = format syles.

print("calender_HTMLCalendar_cssclasses:", calendar.HTMLCalendar().cssclasses)   # it will give the list of the days.

print("calender_HTMLCalendar_cssclasses_noday", calendar.HTMLCalendar.cssclass_noday)  # it will give the extra days of the month from the starting and the ending of the month.

print("calender_HTMLCalendar_cssclasses_weekday_head", calendar.HTMLCalendar().cssclasses_weekday_head)   # it will give the weekdays as the header in the row.

print("calendar_HMLCalender_csscclasses_month_head", calendar.HTMLCalendar().cssclass_month_head)

print("calendar_HTMLCalendar_cssclases_month", calendar.HTMLCalendar().cssclass_month)  # it will give whole months table's.

print("calendar_HTMLCalendar_cssclasses_year", calendar.HTMLCalendar.cssclass_year)     # it will give whole years table.

print("calendar :", calendar.LocaleTextCalendar(firstweekday=0, locale=None))

print(calendar.setfirstweekday(2))


print("cal", calendar.firstweekday())
calendar.setfirstweekday(4)  # we can set the first week day.
print("as", calendar.firstweekday())    # it will give the first week of the day.

print("leaps or not :", calendar.isleap(year=2024))   # it will tells us weather the year is leap year or not.

print("check the leap years :", calendar.leapdays(2000, 2020))  # it will give number of leap years between the years.

print("weekdays :", calendar.weekday(2022, 4, 22))

print("calendar_weekheader :", calendar.weekheader(15))  # it will take width as (number of characters and remaining will takes as spaces).

print("calender_monthrange :", calendar.monthrange(2020, 4))    # it will return tuple(firstweekday, number of days).

print("calendar_monthcalendar:", calendar.monthcalendar(2022, 3))    # returns a list consists of days.

calendar.prmonth(theyear=2022, themonth=4, w=2, l=2)

print(calendar.month(theyear=2022, themonth=8, w=2, l=2))

calendar.prcal(theyear=2022, w=2, l=1, c=6, m=5)

print("calendar_calender :", calendar.calendar(theyear=2022, w=2, l=2, c=2, m=6))

ta = datetime.datetime.now().timetuple()
print(ta)
print(calendar.timegm(ta))  # it will gives the timestamp of a given datetime.

for day_name in calendar.day_name:  # calendar.day_name gives the day names in a full name.
    print("day_name : ", day_name)

for day_abb in calendar.day_abbr:   # calendar.day_abbr gives the day names in a short form.
    print("day_abbr :", day_abb)

for month_name in calendar.month_name:  # calender.month_name gives the month names in a full name.
    print("month_name :", month_name)

for month_abbr in calendar.month_abbr:
    print("month_abbr :", month_abbr)
