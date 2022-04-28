"""The epoch is the point where the time starts, and is platform dependent.
For Unix, the epoch is January 1, 1970, 00:00:00 (UTC).
Write a Python program to find out what the epoch is on a given platform.
Also convert a given time in seconds since the epoch.
"""
import datetime
import time
from datetime import timedelta
d = datetime.datetime.strptime("January 1, 1970, 00:00:00 (UTC)", "%B %d, %Y, %H:%M:%S (%Z)")
print(d.timetuple())
print(time.gmtime(0))
print(time.gmtime(36000))
