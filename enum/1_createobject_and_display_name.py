"""
Write a Python program to create an Enum object and display a member name and value.
Sample data :
Member name: Albania
Member value: 355
"""
from enum import Enum

class object(Enum):
    Albania = 355


print("Member name :", object.Albania.name)
print("Member value :", object.Albania.value)