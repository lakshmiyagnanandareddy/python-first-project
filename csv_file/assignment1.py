"""
Write a Python program to read each row from a given csv file and print a list of strings.
"""
import csv
with open("demo.csv", "r") as demo:
    demo_file = csv.reader(demo)
    for line in demo_file:
        print(line)