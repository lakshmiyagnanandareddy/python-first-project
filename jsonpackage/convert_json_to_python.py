def convert_json_to_python1():
    import json
    open_json = open("..\\jsonfiles\\student_details.json", "r")
    students_python_data = json.load(open_json)
    print(students_python_data)


convert_json_to_python1()
