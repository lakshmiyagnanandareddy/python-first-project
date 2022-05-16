"""
Using filter() and list() functions and .lower() method filter all the vowels in a given string.
"Winter Olympics in 2022 will take place in Beijing China"
"""
my_list = "Winter Olympics in 2022 will take place in Beijing China"
my_list1 = "aeio"

def vowel(my_list):
    vowels = ["a", "i", "e", "o", "u"]
    return vowels if my_list in my_list else ""


print(list(filter(lambda x: True if x.lower() in "aeiou" else False, my_list)))
print(vowel(my_list))