import re
string = "bbbbab"
match_string = re.compile(r"[b]+").finditer(string)
for match in match_string:
    print(match)