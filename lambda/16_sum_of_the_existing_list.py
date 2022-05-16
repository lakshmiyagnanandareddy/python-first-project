"""
Using map() function, first return a new list with absolute values of existing list. Then for ans_1,
find the total sum of the new list's elements.
[99.3890,-3.5, 5, -0.7123, -9, -0.003]
"""
from functools import reduce
my_list = [99.3890, -3.5, 5, -0.7123, -9, -0.003]

print(reduce(lambda x, y: x + y, my_list))
