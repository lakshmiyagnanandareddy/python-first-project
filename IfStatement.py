x = 5 # x assigned as 5
if x == 2:
    print("x is equal to 2")
else:
    print("x is not equal to 2")
###
x = int(input("Enter the x value "))
y = int(input("enter the y value "))
z = int(input("enter the z value "))
if x<y:
    print(x,"is lessthan",y)
elif x==y:
    print(x,"equal to",y)
else:
    print(x,"is greaterthan",y)


#shortHandIf
if x==y: print(x,"equal to",y) # short hand if means total if statement in a single line

#sortHandIfElse
print(x,"equal to",y) if x==y else print(x,"not equal to",y)

##
print(x,"is greaterthan",y) if x>y else print(x,"is lessthan",y) if x==y else print(x,"not eqaul to",y)

### ifStatementWithLogicalOperator
if x>y and y>z:
    print(x,"is greaterthan",y,"and",y,"is greaterthan",z)
else:
    print(x,"is lessthan",y,"and",y,"is lessthan",z)

#nestedIf(ifStatementWhichIncludesInsideAnotherIfStatementIsKnownAs'NestedIf')
if x<y:                                         #NestedIf
    print(x,"is lessthan",y)
    if y<z:
        print(y,"is lessthan",z)
    else:
        print(y,"is greaterthan",z)

#IfstatementCannotBeEmpty,for,ThatIfweWantToKeepEmptyItForAnyReason,weUse"Pass"Keyword.
if x<y:
    pass

