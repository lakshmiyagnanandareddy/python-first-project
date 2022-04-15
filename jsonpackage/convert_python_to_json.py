def convert_python_to_json():
    import json
    student_data = {"students": {'id': '301', 'name': "nandu", "age": 20, "employee": True,
                                 "address": ["Room No: 57", "proddatur", "kadapa", "Andhra pradesh"],
                                 "student_details": {"id": "301", "name": "nandu", "age": 20,
                                                     "address": ["Room No: 57", "prodddatur", "kadapa",
                                                                 "Andhra pradesh"]}},
                    "student2": {"id": "302", "name": "vignesh", "age": 18,
                                 "address": ["Room No: 57", "proddatur", "kadapa", "Andhra pradesh"],
                                 "student_details": {"id": "301", "name": "nandu", "age": 20,
                                                     "address": ["Room No: 57", "prodddatur", "kadapa",
                                                                 "Andhra pradesh"]}},
                    "student3":{"name":"mohan",
                                "age": 50}}

    # open_json = open("..\\jsonfiles\\student_details.json", "r")
    students_json_data = json.dumps(student_data)
    print(students_json_data)
    print(type(students_json_data))
    print(isinstance(students_json_data, dict))
    print(type(student_data))
    print(isinstance(student_data, dict))


convert_python_to_json()
