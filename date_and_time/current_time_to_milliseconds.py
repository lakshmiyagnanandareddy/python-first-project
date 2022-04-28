"""Write a Python program to get current time in milliseconds in Python"""
import datetime
print("Milli seconds : ", datetime.datetime.today().time().hour*datetime.datetime.today().time().minute*datetime.datetime.today().time().second*1000)
# 23716000
# 12100000
# 24200000
