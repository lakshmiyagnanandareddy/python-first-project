"""
Write a Python program to read a given CSV file having tab delimiter.
"""
import csv
with open('demo.csv', 'r') as demo:
    demo_file = csv.reader(demo, delimiter='\t')
    for line in demo_file:
        print(line)