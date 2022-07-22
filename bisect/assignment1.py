"""
Write a Python program to locate the left insertion point for a specified value in sorted order.
"""
import bisect
sorted_list = [22, 43, 67, 78, 99]
print(bisect.bisect_left(sorted_list, 60))
