import ast
"""
ast (module) : 1. It like what the python interperator acts its self if thier is any error while we are running the code
                this will itself modify it and maximum many automated tools will cover the error and tries to give the
                output
               2. Mainly with this module we can see actually what interperator does to the code while running. 
"""
# exec:
laptop = ast.parse("print('its working.')")
print(laptop)
exec(compile(source=laptop, filename="_ast.py", mode="exec"))

# eval:
add = '6+8'
add = ast.parse(source=add, mode="eval")
print(add)
print(eval(compile(add, '', mode="eval")))

# we can understand actually,
# Ex : what ast mean ?, we can observe what interperator does with the code to get the output
print(ast.dump(add))

fruits = ast.parse("""
fruit = ["banana", "jack_fruit"]
name = "vignesh"
for i in fruit:
    print("{} likes {}".format(name, i))
""")
print(ast.dump(fruits))