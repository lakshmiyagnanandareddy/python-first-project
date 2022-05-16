"""
Using map() function and len() function create a list that's consisted of lengths of each element in the first list.
["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]
"""
my_list = ["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]

print("length of item :", list(map(lambda x: len(x), my_list)))
print("items :", my_list)