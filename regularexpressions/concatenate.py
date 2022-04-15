import re
original_string = "Enter at 1 2077 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready."
string = re.compile(r"[1-9]\s[1-9]", flags=re.DEBUG).sub("", original_string)
print(string)
