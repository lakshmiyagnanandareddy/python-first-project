import re
string = "I have given a pen"
print(re.compile(r" ").sub("_", string.lower()))
