"""
 Write a Python program to generate the running product of the elements of an given iterable.
"""
import itertools
import operator

elements = [1, 4, 6, 7, 2]
running_product = itertools.accumulate(elements, operator.mul)
for product in running_product:
    print(product)
