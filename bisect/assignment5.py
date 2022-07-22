"""
Write a Python program to find the index position of the largest value smaller than a given number in a sorted list using Binary Search (bisect).
"""
import bisect
list = [23, 45, 5, 7, 8]
print(list[(bisect.bisect_right(list, 6))-1])
