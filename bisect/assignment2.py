"""
Write a Python program to locate the right insertion point for a specified value in sorted order.
"""
import bisect
sorted_list = [21, 34, 42, 56, 78]
print(bisect.bisect_right(sorted_list, 39))
