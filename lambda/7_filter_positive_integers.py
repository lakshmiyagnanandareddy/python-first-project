"""
This time using filter() and list() functions filter all the positive integers in the string.
"Winter Olympics in 2022 will take place in Beijing China"
"""
my_list = "Winter Olympics in 2022 will take place in Beijing China"

print(list(filter(lambda x: True if x in "0123456789" else False, my_list)))
