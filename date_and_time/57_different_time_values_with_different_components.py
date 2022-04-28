"""
Write a Python program to get different time values with components timezone, timezone abbreviations,
the offset of the local (non-DST) timezone, DST timezone and time of different timezones.
Sample Output:
Default Zone:
TZ : (not set)
Timezone abbreviations: ('UTC', 'UTC')
Timezone : 0 (0.0)
DST timezone 0
Time : 11:30:05 04/13/21 UTC
Pacific/Auckland :
TZ : Pacific/Auckland
Timezone abbreviations: ('NZST', 'NZDT')
Timezone : -43200 (-12.0)
DST timezone 1
Time : 23:30:05 04/13/21 NZST
Europe/Berlin :
TZ : Europe/Berlin
Timezone abbreviations: ('CET', 'CEST')
Timezone : -3600 (-1.0)
DST timezone 1
Time : 13:30:05 04/13/21 CEST
America/Detroit :
TZ : America/Detroit
Timezone abbreviations: ('EST', 'EDT')
Timezone : 18000 (5.0)
DST timezone 1
Time : 07:30:05 04/13/21 EDT
Singapore :
TZ : Singapore
Timezone abbreviations: ('+08', '+08')
Timezone : -28800 (-8.0)
DST timezone 0
Time : 19:30:05 04/13/21 +08
"""
import time
t = time.time()
#print(time)
print("Timezone abbreviations :", time.gmtime(t).tm_zone)
print("Timezone :", time.timezone)
print("DST timezone :", time.gmtime(t).tm_isdst)
print("Time :", time.strftime("%H:%M:%S %D %z"))