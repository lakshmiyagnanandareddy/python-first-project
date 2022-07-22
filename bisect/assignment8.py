"""
Write a Python program to find a triplet in an array such that the sum is closest to a given number.
Return the sum of the three integers.
"""
import itertools
list = [1, 4, 6, 8, 3]
target = 30
reach = 0
for triplet in itertools.combinations(list, 3):
    if sum(triplet) > reach:
        reach = sum(triplet)
        combination = triplet
print(triplet)
print(reach)
