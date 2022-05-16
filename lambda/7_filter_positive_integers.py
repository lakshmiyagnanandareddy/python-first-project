"""
This time using filter() and list() functions filter all the positive integers in the string.
"Winter Olympics in 2022 will take place in Beijing China"
"""
my_list = "Winter Olympics in 2022 will take place in Beijing China"

print(list(filter(lambda x: int(x) > 0, my_list)))