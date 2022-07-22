"""
Write a Python program that reads a CSV file and remove initial spaces, quotes around each entry and the delimiter.
"""
import csv
with open('demo.csv', 'r') as demo:
    demo_file = csv.reader(demo, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for line in demo_file:
        print(line)