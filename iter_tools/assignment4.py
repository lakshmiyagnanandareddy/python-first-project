"""
 Write a Python program to construct an infinite iterator that returns evenly spaced values starting with a specified number and step.
"""
import itertools
infinite_iterator = itertools.count(start=10, step=2)
for number in infinite_iterator:
    print(number)