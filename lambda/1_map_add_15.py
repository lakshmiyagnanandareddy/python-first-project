"""
Write a Python program to create a lambda function with map that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.

Sample Output:
25
48
"""
x = [10]
y = [12]

print("Addition of the 15", list(map(lambda x: x+15, x)))

print("multiplicaton of x and y", list(map(lambda x, y: x * y, x, y)))


