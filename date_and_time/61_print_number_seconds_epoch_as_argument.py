"""
Write a Python program that takes a given number of seconds and pass since epoch as an argument.
Print structure time in local time.
Sample Output:
Result: time.struct_time(tm_year=1983, tm_mon=2, tm_mday=19, tm_hour=21, tm_min=38, tm_sec=18, tm_wday=5, tm_yday=50, tm_isdst=0)
Year: 1983
"""
import time


def epoch(s):
    print(time.gmtime(s))
    print("Year :", time.gmtime(s).tm_year)


epoch(time.time())
