"""
Write a Python program to read a given CSV file as a dictionary.
"""
import csv
with open('demo.csv', 'r') as demo:
    demo_file = csv.DictReader(demo)
    for line in demo_file:
        print(line)