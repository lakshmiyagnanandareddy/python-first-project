"""
This time swap the map() and filter() functions so that map() function is inside filter() function.
Convert a number to positive if it's negative in the list.
Only pass those that are converted from negative to positive to the new list.

[-1000, 500, -600, 700, 5000, -90000, -17500]
"""
my_list = [-1000, 500, -600, 700, 5000, -90000, -17500]

a = list(filter(lambda x: True if x > 0 else False, map(lambda x: x*-1, my_list)))

print(a)
