import bisect
"""
is used to find the suitable index to insert the number,
is used to insert in a sorted manner,
get grades for marks.
"""
li = [0, 3, 2, 1, 6, 4]
print(bisect.bisect(li, 5))  # bisect - is used to find the suitable index to insert the number.
print(li)
bisect.insort(li, 5)    # insort- is used to insert in a sorted manner
print(li)