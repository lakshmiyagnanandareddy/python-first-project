import re
test_string = "Nandu VIgnesh"
print(re.compile(r"[a-z]").sub("",test_string))