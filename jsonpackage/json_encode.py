import json
from json import JSONEncoder


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state


class Encode(JSONEncoder):
    def default(self, o):
        return o.__dict__


student_name = input("Enter your name : ")
student_age = int(input("Enter your age : "))
print("Enter your address details")
address_street_name = input("Enter your street name : ")
address_city = input("Enter your city : ")
address_state = input("Enter your state : ")
address = Address(address_street_name, address_city, address_state)
student = Student(student_name, student_age, address)
student_json_type = json.dumps(student, indent=2, cls=Encode)
print(student_json_type)
print(type(student_json_type))
student_python_type = json.loads(student_json_type)
print(student_python_type)
print(type(student_python_type))
