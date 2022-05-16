"""
This time swap the map() and filter() functions so that map() function is inside filter() function.
Convert a number to positive if it's negative in the list.
Only pass those that are converted from negative to positive to the new list.

[-1000, 500, -600, 700, 5000, -90000, -17500]
"""
my_list = [-1000, 500, -600, 700, 5000, -90000, -17500]


def convert(x):
    return map(lambda x: x + (x+x), x)


a = list(filter(lambda x: convert(x) if x < 0 else _, my_list))

print(a)