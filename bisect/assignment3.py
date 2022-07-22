"""
Write a Python program to insert items into a list in sorted order.
"""
import bisect
lis = [2, 1, 10, 5, 9, 6]
sorted_list = []
for number in lis:
    bisect.insort(sorted_list, number)
print(sorted_list)