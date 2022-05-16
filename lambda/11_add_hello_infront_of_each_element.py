"""
Write a map function that adds "Hello, " in front of each item in the list.
["Jane", "Lee", "Will", "Brie"]
"""
my_list = ["Jane", "Lee", "Will", "Brie"]
print(list(map(lambda x:("Hello," + x), my_list)))