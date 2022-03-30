def introduction():
    # Introduction about program
    print("The program will gives the sum,substraction,multiplication,division, of the two numbers")


def inpu():
    # Taking the input from the user
    num1 = int(input("enter the first number : "))
    c = int(input("enter the second number : "))
    g = int(input("enter the third number : "))

    return num1, c, g


def addition(num1, d):
    # addition
    print("The sum of the two numbers :", num1 + d)


def substracton(num1, num2):
    # substraction
    print("The substraction of the two numbers :", num2 - num1)


def multiplication(num1, num2):
    # multiplication
    print("The multiplication of the two numbers :", num1 * num2)


def division(num1, num2):
    # division
    print("the division of the two numbers :", num1 / num2)


def main():
    introduction()
    a, n, c = inpu()
    addition(a, n)
    substracton(a, n)
    multiplication(a, c)
    division(a, c)


main()

#Global canstant
print("Global constant")
number = 100 #global constant value which means 100-value is assigned for number for all functions
def constant():
    print("Number is ", number)


def Addition():
    print("Addition is ", number + number)


constant()
Addition()
def randomfuntions():
    # choice random from the list only
    import random
    a = ["abg", "cfv", "bgf", 1, 2, 3, 4]
    print(random.choice(a))
    # choices random from the list with given probability(in weights) and next it will print that meany times
    import random
    a = ["axvd", "adda", "ascdc", "abh"]
    print(random.choices(a, weights=[3, 4, 6, 8], k=10))
    # sample-returns the given limit values in a random sequence
    import random
    my_list = ["lakshmi", "dad", "mom", "nk", 7, 8]
    print(random.sample(my_list, k=3))
    # random-it returns random value between(0.1 to 0.9)
    import random
    print(random.random())
    # uniform-it returns random floating number between (a,b)
    import random
    print(random.uniform(20, 40))
    # triiangular-it returns the value with more chances of nearest number(20-low,190-high,50-high probablity of nearest number
    import random
    print(random.triangular(20, 190, 50))
