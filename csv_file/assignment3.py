"""
Write a Python program to read a given CSV file as a list.
"""
import csv
with open('demo.csv', 'r') as demo:
    demo_file = csv.reader(demo)
    print(list(demo_file))