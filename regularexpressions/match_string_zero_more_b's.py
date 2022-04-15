import re
test_string = "babbbbb"
string = re.compile(r"[b]*").finditer(test_string)
for match in string:
    print(match)
