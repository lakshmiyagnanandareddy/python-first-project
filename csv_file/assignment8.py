"""
Write a Python program that reads each row of a given csv file and skip the header of the file.
Also print the number of rows and the field names.
"""
import csv
with open('demo.csv', 'r') as demo:
    demo_file = csv.reader(demo)
    fields = next(demo_file)
    for line in demo_file:
        print(line)
    print(demo_file.line_num)
    print(fields)