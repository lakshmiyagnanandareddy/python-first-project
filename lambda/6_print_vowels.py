"""
Using filter() and list() functions and .lower() method filter all the vowels in a given string.
"Winter Olympics in 2022 will take place in Beijing China"
"""
my_list = "Winter Olympics in 2022 will take place in Beijing China"


def vowel(my_list):
    vowels = ["a", "i", "e", "o", "u"]
    return vowels if my_list in my_list else ""


vowels = ["a", "i", "e", "o", "u"]
print(list(filter(lambda x: x == vowels, my_list)))
