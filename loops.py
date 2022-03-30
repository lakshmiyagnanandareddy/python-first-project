#whileLoop
numbers = int(input("Please enter the number you want to print "))
initialValue = 0
while initialValue<=numbers:
    print(initialValue)
    initialValue=initialValue+1
print("hi")

#forLoop
for i in [1,2,3,4]:
    print(i)
print("completed printing i values")

##forLoopString
for i in "abc":
    print(i)


#forLoopRange
for i in range(5,10,2):
    print(i)
    print("hi")

#nestedloop - the loop which includes inside other loop
for i in range(4):
    for i in range(6):
        addition = i + j
        print(addition)

#sentinel-it will take the input continously until we enter the stop value.
number = int(input("enter the number to display "))
print(number)
while number != 0:
    print("Enter 0 to stop display numbers")
    number = int(input("enter the number to display "))
    print(number)
print("Thanks")

#input vaildation - To check weather the given is correct are not.
print("please enter the number ")
number = int(input())
while number < 0:
    print("please enter positive number")
    number = int(input())
print("Successfully completed your task")