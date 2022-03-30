# list- it is represented by [],it can be changeable
# tuple- it is represented by (),it cannot changable
lisT = ["a", 1, 4, "3"]
print(lisT)

print(lisT[1])  # inside bracket's it mention the index of the list to print

print(lisT[-1])  # inside brackets wile using "-" for index it will start from last

print(len(lisT))  # len - keyword is used to count the words present inside the list

my_list = list(range(5))  # we have to include list keyword at the starting, if we want to give a like range
print(my_list)


m = my_list[3]
print(m)


for i in my_list:
    print(i)


#sales ex
def salesEx():
    sales = int(input("how many days you have the sales in the shop"))
    sals = list()
    for i in range(sales):
        print("Enter the sales amount of the day", i + 1)
        sale = int(input())
        sals.append(sale)
    print(sals)

#
def ab():
    print("ab")
    my_lis = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
    i = 6
    if i in my_lis:
        print("we found", i)


myList = [1, 23, 4, 5, 6, 9, 8, 3]
print(myList[1:5])  # it will print from index 1 to 4.
print(myList[:4])  # it will print from starting index to 3index.
print(myList[2:])   # it will print from the 2index to end of the index.
myList[3] = 100
print(myList)


# Ex
def ex():
    highest_score = 0
    num_score = int(input("Enter the number of player score "))
    player_score = list()
    for i in range(num_score):
        print("Enter the player score", i + 1)
        score = int(input())
        player_score.append(score)
        if highest_score < player_score[i]:
            highest_score = player_score[i]
    print("the highest score is",
          highest_score)


# tuple
subject_tuple = ("maths", "chemistry", "physics")
print(subject_tuple)
for i in subject_tuple:
    print(i)

subject_list = list(subject_tuple)  # converted tuple into list
print(subject_list)

converted_tuple = tuple(subject_list)   # converted list to tuple
print(converted_tuple)


# Exception
try:
    print("Enter the number")
    number = int(input())
    print(ksy)
except ValueError:  # used for wrong data type error
    print("you have entered a wrong number form")
except:
    print("wrong format")


# error
def error():
    repeat = True
    while repeat == True :
        try:
            number = int(input("Enter the number for the error "))
            print(number)
            repeat = False
        except:
            print("wrong entry")
            repeat == True

error()
