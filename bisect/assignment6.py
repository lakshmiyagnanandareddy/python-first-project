"""
Write a Python program to find the index position of the last occurrence of a given number in a sorted list using Binary Search (bisect). Go to the editor
Expected Output:
Last occurrence of 8 is present at 5
"""
import bisect
list = [8, 8, 23, 44, 57, 78, 89]
print(bisect.bisect_right(list, 8)-1)
