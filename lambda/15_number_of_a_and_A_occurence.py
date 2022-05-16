"""
Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a.
["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
"""
my_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

print("list :", my_list)
print("a - consists of :", list(map(lambda x: x.count("A"), my_list)),  "\nA - consists of :", list(map(lambda x: x.count("A"), my_list)))