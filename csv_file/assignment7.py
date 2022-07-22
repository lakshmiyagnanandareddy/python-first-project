"""
Write a Python program to read specific columns of a given CSV file and print the content of the columns.
"""
import csv
with open('demo.csv', 'r') as demo:
    demo_file = csv.DictReader(demo)
    for line in demo_file:
        print(line['email'])