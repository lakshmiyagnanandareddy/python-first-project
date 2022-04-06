def waste():
    import json
    import sys
    json_file = open("Json.json", "r")
    json_data = json_file.read()
    students_obj = json.loads(json_data)
    a = json.dumps(students_obj, indent="\t", separators=(",", ":"), sort_keys=False)   # indent=will give indentation in every distribution
    # student_objj = student_obj["a"]                    # seperator=will have two arguments(keyvalue,between:key and value)
    # print(students_obj["id"])
    # print(sys.getsizeof(obj))
    # print(len(obj))

    print(a)

    # for student in


def convert_json_to_python1():
    import json
    open_json = open("Json.json", "r")
    python = json.load(open_json)
    print(python)


def convert_json_to_python2():
    import json
    json_input = {'students': {'id': '301', 'name': 'nandu', 'age': 20, "employee": True, 'address': ['Room No: 57', 'proddatur', 'kadapa', 'Andhra pradesh'], 'student_details': {'id': '301', 'name': 'nandu', 'age': 20, 'address': ['Room No: 57', 'prodddatur', 'kadapa', 'Andhra pradesh']}}, 'student2': {'id': '302', 'name': 'vignesh', 'age': 18, 'address': ['Room No: 57', 'proddatur', 'kadapa', 'Andhra pradesh'], 'student_details': {'id': '301', 'name': 'nandu', 'age': 20, 'address': ['Room No: 57', 'prodddatur', 'kadapa', 'Andhra pradesh']}}}
    python = json.dumps(str(json_input))
    print(python)


def indentation_and_sort_key():
    import json
    open_json_file = open("Json.json", "r")
    json_file = json.load(open_json_file)
    # python = json.dumps(json_file, indent=4, sort_keys=True)
    print(json_file)
    isinstance()


def encode():
    class Employee:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    employee = Employee("nandu", 23)


    def encoder(o):
        if isinstance in
