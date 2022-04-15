import re
string = "abcAB12"
match_string = re.compile(r"\w+").match(string)
if string == match_string.group():
    print("it contains only[a-zA-Z1-9]")

