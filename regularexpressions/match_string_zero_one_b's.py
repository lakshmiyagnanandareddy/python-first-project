import re
test_string = "abbbcABbbC123"
print("followed by one b :")
print(re.compile(r"b{1}").findall(test_string))     # followed by one "b".
print("followed by three b's :")
print(re.compile(r"b{3}").findall(test_string))     # followed by three "b".
print("followed by two to three b's :")
print(re.compile(r"b{2,3}").findall(test_string))   # followed by two to three "b".
