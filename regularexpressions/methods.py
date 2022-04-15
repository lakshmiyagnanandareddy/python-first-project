import re
test_string = "abcbrvrabc234abc123""abc""abc"
matches = re.compile("b").finditer(test_string)
print(matches)
for i in matches:
    print(i)

string = "\n"
print(string)   # here \n - represents to go nextline.
print(repr(string))     # Here if we use repr function (or) r"\n" it will convert as a raw string.

test_string = "abcdefghiabc123abc"
matches = re.compile("abc").findall(test_string)    # findall() - will find the compile pattern in the object.
print(matches)

test_string = "abcabcedfabc"
match = re.compile("abc").match(test_string)     # match() - will find the compile pattern in the object from the starting index.
print(match)
match2 = re.compile("bc").match(test_string)
print(match2)
search = re.compile("bc").search(test_string)   # search() - will find the compile pattern in the object from any index but it will return only once.
print(search)

print("search methods :")
test_string = "abcdefgha@bcijklabc""abc""abc"
matches = re.compile("abc").finditer(test_string)
for match in matches:
    print(match.span(), match.start(), match.end(), match.group())
# span() - will print starting and the ending index of compile pattern.
# start() - will print starting index of compile pattern.
# end() - will print ending index of the compile pattern.
# group() - will print the searching string.

print("meta characters :")
test_string = "abc123 def_ abc4  1abc2 56abc dabc -"
matches = re.compile(".").finditer(test_string)     # if we provide "." in compile it will print all characters in the string.
for match in matches:
    print(match)
    print(match.group())

matches = re.compile("^abc").finditer(test_string)     # if we provide "^" in compile it will search character from starting.
for match in matches:
    print(match)

matches = re.compile("abcd$").finditer(test_string)     # if we provide "$" in compile it will search character from ending of the string.
for match in matches:
    print(match)

print("special characters :"
      "\n")
print(r"\d")
matches = re.compile(r"\d").finditer(test_string)   # "\d" - it will search matches for numeric digits [0-9] in the string.
for match in matches:
    print(match)

print(r"\D")
matches = re.compile(r"\D").finditer(test_string)  # "\D" - it will search matches for non-numeric digits in the string.
for match in matches:
    print(match)

print(r"\s")
matches = re.compile(r"\s").finditer(test_string)   # "\s" - it will search matches for white space in the string.
for match in matches:
    print(match)

print(r"\S")
matches = re.compile(r"\S").finditer(test_string)  # "\S" - it will search matches for non-white space in the string.
for match in matches:
    print(match)

print(r"\w")
matches = re.compile(r"\w").finditer(test_string)   # "\w" - it will search matches for alphanumerics in the string.
for match in matches:
    print(match)

print(r"\W")
matches = re.compile(r"\W").findall(test_string)   # "\W" - it will search matches for non-alphanumerics in the string.
print(matches)

print(r"\b")
matches = re.compile(r"abc\b").findall(test_string)     # "\b" - it will search compile pattern from the starting or ending of the blocks.
print(matches)

print(r"\B")
matches = re.compile(r"\Babc\B").findall(test_string)   # "\B" - opposite to "\b"
print(matches)

print("sets"
      "\n")
matches = re.compile(r'[ab]').finditer(test_string)    # []- what we given inside the set it will search.
for match in matches:
    print(match)

matches = re.compile("[1-9-]").finditer(test_string)
for match in matches:
    print(match)
print()
matches = re.compile("[a-zA-Z1-9]").finditer(test_string)
for match in matches:
    print(match)

print("Quantifier :"
      "\n")
test_string = "abc _123 12"

print(r"*")
matches = re.compile(r"\d*").finditer(test_string)  # Here '*' will search for 0 (or) more in the blocks.
for match in matches:
    print(match)

print(r"+")
matches = re.compile(r"_\d+").finditer(test_string)    # Here "+" will search for 1 (or) more in the blocks.
for match in matches:
    print(match)

print(r"?")
matches = re.compile(r"_?\d").finditer(test_string)     # Here "?" will make search compile as optional.
for match in matches:
    print(match)

print({})
matches = re.compile(r"\d{1,4}").finditer(test_string)  # Here "{}" will give that many values in the compile pattern.
for match in matches:
    print(match)

print("dates :")
dates = """
        hello
        2012-02-22
        
        2000-04-23
        2022-04-24
        2021-03-22
        2022-05-28
        
        2022/12/22
        2000/20/12
        2023'20'11
        """
matches = re.compile(r"\d{4}[-/][0-1][1-9][-/]\d{2}").finditer(dates)
for match in matches:
    print(match)

print("names :")
names = """
        hello
        Mr. nandu
        Mr sudharshan
        Mrs. subhadra
        Mr vignesh
        Ms mounika
        """
matches = re.compile(r"(Mr|Mrs|Ms)\.?\s\w+").finditer(names)    # "|" - condition which will chose in optional.
for match in matches:
    print(match)

print("gmail :")
gmail = """
        mlynreddy@gmail993.com
        mudhireddynandu99481@gma-il.com
        srmvrmlynr993@hotmail.com
        """
matches = re.compile(r"([a-zA-Z1-9]+)@([a-zA-Z1-9-]+)\.([a-zA-Z]+)").finditer(gmail)
for match in matches:
    print(match.group(0))   # grouping - group() will give out in the seperated groups.
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

print("modification :")
print("split")
split = "123bds345bcd543bds342"
splited = re.compile("b").split(split)  # split - will separate the test string of the compile pattern so,it will split that much parts.
print(splited)

print("sub")
test_string = "Hello nandu, nandu are you still alive"
sub = re.compile("nandu").sub("OMG", test_string)
print(sub)

print("URlS")
Urls = """
        http://www.youtube.com
        https://www.fb.com
        www.whats-up.com
        """
url = re.compile(r"(https?://)?www\.([a-zA-Z-]+)(\.com)").finditer(Urls)
for urel in url:
    print(urel)

sub = re.compile(r"(https?://)?www\.([a-zA-Z-]+)(\.com)").sub(r"\2\3", Urls)
print(sub)
