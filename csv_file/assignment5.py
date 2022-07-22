"""
Write a Python program to read a given CSV files with initial spaces after a delimiter and remove those initial spaces.
"""
import csv
with open('demo.csv', 'r') as demo:
    demo_file = csv.reader(demo, skipinitialspace=True)
    for line in demo_file:
        print(line)
print()
with open('demo.csv', 'r') as demo:
    demo_file = csv.reader(demo, skipinitialspace=False)
    for line in demo_file:
        print(line)