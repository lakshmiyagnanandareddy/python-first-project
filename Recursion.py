def main():
    def recursion(k):   # recursion - repeat
        if k > 0:
            print('This is', k)
            k = k-1
            recursion(k)
    k = int(input("Enter the recursion number : "))

    recursion(k)


def mainex():
    def recursion(factorial):
        if factorial == 0:
            return 1
        else:
            return factorial * recursion(factorial-1)

    def main():
        factorial = int(input("Enter the factorial number : "))
        print("The factorial number of the", factorial, "is", recursion(factorial))

    main()


def mainex2():

    def choice():
        choicee = int(input())
        if choicee != 1 and choicee != 2:
            print("Wrong entry!!")
            print("Enter either 1 or 2")
            return choice()
        return choicee

    def main(choice):
        print("Enter the corresponding number", "\n", "1.Add money to the batches", "\n", "2.Transfer money to the batches")
        choice = choice()
        batch = []
        if choice == 1:
            no_batches = int(input("Enter the number of batches you would like to add : "))
            for i in range(no_batches):
                print("enter the amount of batch", i+1, ":")
                add_batches = int(input())
                batch.append(add_batches)
            print("your data has been successfully saved!!")
            choice = input("If you want to go for transfer batches 'y' - yes and 'n' - no : ")
            if choice.lower() == "y":
                choice = 2

        if choice == 2:
            print("no.of batches you want to transfer")
            print("Starting batch :")
            starting_batches = int(input())
            print("last batch :")
            ending_batch = int(input())
            starting_batches -= 1
            ending_batch -= 1
            total = batch_sum(starting_batches, ending_batch, batch)
            print("This is the total amount you had transfer $", format(total, ",d"), sep="")

    def batch_sum(starting_batches, ending_batch, batch):
        if ending_batch >= starting_batches:
            return batch[ending_batch]+batch_sum(starting_batches, ending_batch-1, batch)
        else:
            return 0

    main(choice)


def recursion():    # compare to recursion_loop.normal loop is very faster in the execution time.
                    # compare to normal_loop.recursion_loop is easy to design a program.
    def loop():
        fibonacci = [0]*10
        print("loop in fibonacci :")
        print("0")
        for i in range(10):
            if i == 0:
                fibonacci[i] = 1
            elif i == 1:
                fibonacci[i] = 1
            else:
                fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
            print(fibonacci[i])

    def function(n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return function(n-1) + function(n-2)

    def recursive_loop():
        print("This is the recursive loop of 10 numbers :")
        print("0")
        for i in range(10):
            print(function(i))

    loop()

    recursive_loop()


def interview():
    list = [-1, 1, 34, 5]
    biggest_number = 0
    for i in list:
        if i > biggest_number:
            biggest_number = i

    for i in list:
        while (i < biggest_number) and (i >= 0):
            biggest_number = i

    print(biggest_number)


def interview2():
    def construct(a, b):
        def pair(x):
            return x(a, b)
        return pair

    def first(pair):
        def x(a, b):
            return a
        return pair(x)

    def last(pair):
        def x(a, b):
            return b
        return pair(x)

    a = int(input("Enter the first element : "))
    b = int(input("Enter the last element : "))
    print("This is the first element : ", first(construct(a, b)))
    print("This is the last element : ", last(construct(a, b)))


def interview3():
    def add(lis, k, n):
        if n == len(lis):
            return False
        j = 0
        for i in range (n+1, len(lis)):
            if lis[i] + lis[n] == k:
                j = 1
                break
        if j == 1:
            return True
        return add(lis, k, n+1)
    print("Enter the 'k' value : ")
    n = 0
    k = int(input())
    again = "y"
    lis = []
    while again == "y":
        list_number = int(input("This number will add to the list :"))
        lis.append(list_number)
        again = input("if you want to add another to the list 'y'- yes or 'n'- no")
    print(lis)
    print(add(lis, k, n))


def interview3():
    def multiple(my_lis, first_number, i, j, new_lis, k):
        if i+1 >= len(my_lis):
            j = j+1
            new_lis.append(first_number)
            first_number = my_lis[0]
            i = 0
            if j - 1 == len(my_lis):
                print(new_lis)
            if j-1 <= len(my_lis):
                multiple(my_lis, first_number, i, j, new_lis, k)
        elif my_lis[j] == my_lis[i]:
            k=0
            multiple(my_lis, product, i + 1, j, new_lis, k)
        else:
            product = first_number * my_lis[i + 1]
            multiple(my_lis, product, i + 1, j, new_lis, k)

    def main():
        product = 0
        again = "y"
        my_lis = []
        new_lis = []
        j = 0
        i = 0
        k = 0
        while again == "y":
            list_number = int(input("Enter a number that will be added to the list"))
            my_lis.append(list_number)
            again = input("if you want to add another number to the list 'y' - yes or 'n' - no : ")
        first_number = my_lis[0]
        multiple(my_lis, first_number, i, j, new_lis, k)
    main()


def counting_by_2(number):
    if number == 0:
        return print("zero")
    for i in range(number):
        print("*", end=" ")
    print("")
    counting_by_2(number-2)

#    if number > 0:
#counting_by_2(number-2)


def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)


number = 5
print(factorial(number))


def fibonacci(count, number, first_number, second_number):
    if count == 0 <= number:
        print(first_number)
        return fibonacci(count+1, number, first_number, second_number)
    elif count == 1 <= number:
        print(second_number)
        return fibonacci(count+1, number, first_number, second_number)
    elif number >= count:
        print(first_number + second_number)
        return fibonacci(count+1, number, second_number, first_number+second_number)

"""
count = 0
number = int(input("Enter the number of fibonacci numbers :"))
first_number = 0
second_number = 1
fibonacci(count, number, first_number, second_number)
"""

def reverse_string(string):
    if string[-1] == string[0]:
        return string[0]
    return reverse_string(string[1:]) + string[0]


print(reverse_string("Desert"))


def seperate(lis1, lis2, lis3):
    if len(lis3) == 0:
        print(lis1[2])
        lis3.append(lis1[2])
        lis1.remove(lis1[2])
        return seperate(lis1, lis2, lis3)
    elif len(lis2) == 0:
        lis2.append(lis1[1])
        lis1.remove(lis1[1])
        print("lis1", lis1)
        print("lis1", lis2)
        print("lis1", lis3)


lis1 = [0, 1, 2]
lis2 = []
lis3 = []
seperate(lis1, lis2, lis3)