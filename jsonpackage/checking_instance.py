import json
open_json = open("..\\jsonfiles\\student_details.json", "rb")
student_details_pythonDataType = json.load(open_json)
student_details_jsonDataType = json.dumps(student_details_pythonDataType, indent=2)
print(student_details_jsonDataType)
print("The data contains is complex : ", isinstance(student_details_jsonDataType, complex))

