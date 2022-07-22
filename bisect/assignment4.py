"""
Write a Python program to find the first occurrence of a given number in a sorted list using Binary Search (bisect).
"""
import bisect


def occur(list, occur_number):
    index = bisect.bisect_left(list, occur_number)
    if index != len(list) and list[index] == occur_number:
        return print(occur_number, "is at :", bisect.bisect_left(list, occur_number), "index")
    return print(occur_number, "is not present in the list.")


list = [1, 33, 45, 56, 56, 67, 89]
occur(list, 100)