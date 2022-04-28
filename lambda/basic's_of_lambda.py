double = lambda x: x * 2
print(double(2))

smaller = lambda a, b: a if a < b else b

print(smaller(1, 5))

print((lambda a, b: a+b)(1, 4))

add = lambda a, b, c: a+b+c
print("add :", add(a=3, b=30, c=20))

addition = lambda *num: sum(num)    # *num - it will take the number of arguments.
print("addition :", addition(1, 5, 40, 23, 44))

higher_ord_fun = lambda x, fun: x + fun(x)
print("higher_ord_fun :", higher_ord_fun(7, lambda x: x * x))

print((lambda x: (x % 2 and "even" or "even"))(144))    # it is like if else condition,if the condition is true gies even else odd.

find = lambda string: string in "welcome to the innovative world!!"
print("find :", find("to"))

num = [1, 2, 3, 4, 5, 4, 3, 3, 1, 8]
greater = list(filter(lambda num: num < 4, num))
print(greater)
greater.sort()
print(greater)

print(list(filter(lambda num: num % 4 == 0, num)))  # filter - it checks the given condition is true or falseto the list, if true it return the value.

print(list(map(lambda double: double*2, num)))  # map - apply same function to each element of the list

print(list(map(lambda x: pow(x, 2), (2, 4, 8))))


from functools import reduce

num = [1, 2, 5, 9, 3]
print("reduce in addition", reduce(lambda x, y: x + y, num))    # reduce - it will give total in one condition.


def quadratic(a, b, c):
    return lambda x: a*pow(x, 2) + b*x + c


fun = quadratic(1, 3, 5)
print(fun(1))
