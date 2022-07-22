"""
 Write a Python program to generate the running maximum, minimum value of the elements of an iterable.
"""
import itertools
elements = [9, 2, 10, 1, 11, 3]
print(list(itertools.accumulate(elements, max)))
print(list(itertools.accumulate(elements, min)))
