"""
Write a Python program to make an iterator that drops elements from the iterable as soon as an element is a positive number.
"""
import itertools
elements = [-1, -2, 4, -2, 2, 1]
positive_numbers = itertools.takewhile(lambda x: x < 0, elements)
print(list(positive_numbers))