import re
test_string = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for match in test_string:
    matches = re.compile(r"(\w+)( (\(\.com\)))?").finditer(match)
    for ma in matches:
        print(ma.group(1))
