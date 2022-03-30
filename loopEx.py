print("welcome to weather forcast")
print("Monday's temperature ")
monday = int(input())
print("Tuesday's temperature ")
tuesday = int(input())
print("Wednesday's temperature ")
wednesday = int(input())
print("Thursday temperature ")
thursday = int(input())
print("Friday temperature ")
friday = int(input())
print("Saturday temperature ")
saturday = int(input())
print("Sunday temperature ")
sunday = int(input())
coldest_day = 0
hottest_day = 0
days = (monday, tuesday, wednesday, thursday, friday, saturday, sunday)
for i in (days):
    if i <= coldest_day:
        coldest_day = i
    else:
        hottest_day = i
print("coldest day", coldest_day)
print("hottest day", hottest_day)

#leapYear
print("Leap year")
year = int(input("Enter the year "))
if (year % 4 == 0) and (year % 100 !=0):
    print(year,"is a leap year")
elif(year % 100 ==0) and (year % 400 ==0):
    print(year, "is a leap year")
else :
    print(year, "is not a leap year")

#fabinoSeries
print("fabino numbers")
fabinoNumber = int(input("Enter fabino upto fabino numbers you want "))
count = 0
count1 = 1
print(count)
for i in range(1, fabinoNumber):
    c = count1+count
    count = count1
    count1 = c
    print(c)

#starProgram
stars = int(input("Enter the number of stars you want "))
for i in range(1, stars//2):
    for j in range(0, stars//2):
        if j<i and i<=stars//2:
            print("*", end="")
    print(" ")
for i in range(1, stars):
    for j in range(stars//2, 0, -1):
        if j>i:
            print("*", end="")
    print("")

#reverseANumber
number = int(input("Enter number to reverse"))
while 9 < number:
    reverse = number % 10
    print(reverse, end = "")
    number = number//10
print(number)

#pailodrome
number = int(input("Enter number to reverse"))
originalNumber = number
while 9 < number:
    reverse = number % 10
    #reversed = (reverse, end = "")
    number = number//10
#if originalNumber == (reversed,number)

#sentinel
print("Enter the weight of the item")
print("or Enter 0 if you want to save the data into the shipment file")
weight = int(input())
print(weight)
print()
while weight != 0:
    print("Enter the weight of the item")
    print("or Enter 0 if you want to save the data into the shipment file")
    weight = int(input())
    print(weight)
print("The data has been saved into the shipment")







