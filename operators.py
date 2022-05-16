x = int (input( "please enter an 'x' number "))
y = int (input( "please enter an 'y' number "))
addition = x + y
substraction = x - y
multiplication = x * y
division = x/y # quotient
modulus = x%y # reminder
exponention = x**y
floorDivision = x//y # it will give division which is in whole numbers

print("addition", addition)
print("substraction", substraction)
print("multipication", multiplication)
print("division", division)
print("modulus", modulus)
print("exponention", exponention)
print("floor division", floorDivision)

# assignment operators
x += 5 # x+=5 : x = x+5
print("addition in an assignment operator", x)
x -= 5 # x-=5 : x = x-5
print("substraction of an assignment operator", x)
x *= 5 # x*=5 : x = x*5
print("multiplication of an assignment operator", x)
x /= 5 # x/=5 : x = x/5
print("division of an assignment operator", x)
x %= 5 # x%=5 : x = x%5
print("modulus of an assignment operator", x)
x **= 5 # x**=5 : x = x**5
print("exponention of an assignment operator", x)
x //= 5 # x//=5 : x = x//5
print("floor division of an assignment operator", x)
x &= 5 # x&=5 : x = x&5
print("bitwise_and of an assignment operator", x)
x |= 5 # x|=5 : x = x|5
print("bitwise_or of an assignment operator", x)
x ^= 5 # x^=5 : x = x^5
print("bitwise_nor of an assignment operator", x)
x <<= 5 # x<<=5  ; x = x<<5
print("bitwise_left_shift of an assignment operator", x)
x >>= 5 # x>>=5 ; x = x>>5
print("bitwise_right_shift of an assignment operator", x)

#comparison_operators
print("x value is",x)
print("x > y is",x > y)
print("x < y is",x < y)
print("x <= y is",x <= y)
print("x >= y",x >= y)
print("x == y",x == y) #if x is equal to y it returns true
print(" x != y",x != y)#if x is not equal to y it returns true

#logical_operators
print("x value is",x)
print("x < y 'and' x > y is",x < y and x >y) # it returns true if both the conditions are true
print("x > y 'or' x < y is", x > y or x < y) # it returns true if any one condition is true from both conditions
print("'not' (x < y and x > y) is ",not(x < y and x>y)) # it reverses the correct answer

# membership_operators
print("x value 'is'",x)
print(1,2,3,4,5,6,7,8,9)
z = 1,2,3,4,5,6,7,8,9
print("x 'in' above list",x in z) # if the x number is present in the z integers it returns true else false
print("x 'not' in the above list",x not in z) # if the x value is not present in the z integers it returns true else false

#identity_operator
   ### to find the address of object "syntax-id()"
print("x 'is' y",x is y) #it compares the address of x and address of y
#for primitive data types-int,float,string,double,etc..it remains same address for both x and y value beacuese it is in int
# non-primitive data types-list,etc..it remains different addressif it have same values (or) different values inside the list
print("x 'is not' y",x is not y) #it compares the address of x and address of y

