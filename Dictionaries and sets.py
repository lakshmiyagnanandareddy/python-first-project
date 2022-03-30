dictionaries = {"nandu": 3, 'vin': 4, }
print(dictionaries["nandu"])

if "vin" not in dictionaries:
    print("vin not present in dictionaries")
else:
    print(dictionaries["vin"])


for i in dictionaries:
    print(i, dictionaries[i])

# dictionary creation keyword
created_dictionary = dict()  # "dict()" is the keyword creates dictionary
created_dictionary["Dad"] = 50
print(created_dictionary)


# dictionary length
length_dictionary = {"a": 4, "d": 2, "u": 4}
print(len(length_dictionary))


# ...
ex = {"a": [1, 2, 3, 4], "nan": [2, 3]}
ex1 = ex.get("a", "not found")
ex2 = ex.get("nan", "not found in nan")
print(ex)
for i in ex["nan"]:
    print(i)
ex.clear()  # "clear" the key and values in the dictionary will be cleared
print(ex)


print(ex1, ex2)  # "get" is the key  which takes the value of the key (key,if key not found in the dictionay "it print that matter")

# def_ex
ex8 = {"john": 29, "macky": 30, "chicha": 49}
print(ex8.items())  # dictionary items converted into tuples for 'key,value'
for k, v in ex8.items():
    print(k, v)

for i in ex8.keys():  # it takes keys in the dictionary
    print(i)

for i in ex8.values():
    print(i)

def sets():
    print("def sets")
    ex_set = set("abc")
    print(ex_set)   # it will give set with random writing.
    ex_set1= set([1, 2, 4, "avf"])
    print(ex_set1)
    print(len(ex_set))
    print(len(ex_set1))
    ex_set.add(5)   # ".add()"is used to add any one element (or) any to the set.
    print(ex_set)
    ex_set.add("vdvd")
    print(ex_set)
    ex_set.update([1, 3, 6, 7])  # ".update" is used to add one (or) morethan one to the set.
    print(ex_set)
    ex_set.remove(6)    # ".remove" is used to remove one element to the set.it cause an error,if the number is not present in the set.
    print(ex_set)
    ex_set.discard(10)  # ".discard" is used to remove an element.it doesn't cause any error,if number is not present in the set.
    print(ex_set)
    ex_set2 = set([1, 2, 3, 4])
    print(ex_set2.union(ex_set))    # ".union" compares the both set and print union of the sets.
    print(ex_set2.intersection(ex_set))  # ".intersection" compares the both set and print intersection of the sets.

def ex():
    import pickle
    Y = "y"
    y = "y"
    Add = "add"
    while Y == y:
        # students = int(input("Enter the number of students in the class : "))
        print("First enter the score of the student and next enter student name")
        dictionary = dict()
        # for i in range(students):
        add = input("please enter 'add' or 'read' if you want to enter students again")
        if "add" == add:
            dictionary[input("student name : ")] = int(input("score : "))
            print(dictionary)
        add = input("please enter 'add' or 'read' if you want to enter students again")
        # if "add"== add :
            # some = dictionary[input("student name : ")] = int(input("score : "))
            # dictionary.add(some)
        my_file = open("student.txt", "wb")
        pickle.dump(dictionary, my_file)


ex()
