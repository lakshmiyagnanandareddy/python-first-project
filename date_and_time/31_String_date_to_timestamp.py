"""
Write a Python program to convert a string date to the timestamp.
"""
import datetime
print(datetime.datetime.strptime("2022 03 03", "%Y %m %d").timestamp())
