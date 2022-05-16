"""
Using map() function and lambda and count() function create a list which consists of the number of occurence of letter: a.
["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
"""
my_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

print("list :", my_list)
print("number of a occurrence in the item : ", list(map(lambda x: x.count("a"), my_list)))