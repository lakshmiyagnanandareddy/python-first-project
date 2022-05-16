"""
Using filter() and Lambda functions filter the list so that only negative numbers are left.
[12, -1, 9, 8, -0.5, -0.2, -100]
"""
my_list = [12, -1, 9, 8, -0.5, -0.2, -100]
print(list(filter(lambda x: x < 0, my_list)))