"""
Write a Python program to create an iterator to get specified number of permutations of elements.
"""
import itertools
elements = ['a', 'b', 'c', 'd']
permut = itertools.permutations(elements, 2)
for number_of_permut in permut:
    print(number_of_permut)