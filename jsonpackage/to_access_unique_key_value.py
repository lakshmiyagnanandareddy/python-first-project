import json
open_student_details = open("..\\jsonfiles\\student_details.json", "rb")
student_details_pythonDataType = json.load(open_student_details)
name = student_details_pythonDataType["students"]["name"]
print(name)
print(student_details_pythonDataType)

unique = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# unique_key = json.loads(unique)
# {'a': 4, 'b': 2}
# unique_key_value = unique["a"]
print(unique)
print(type(unique))

