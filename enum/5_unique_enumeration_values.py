"""
Write a Python program to get the unique enumeration values.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
"""
import enum
from enum import unique


@unique     # it will raise value error, if there is any duplicate enum-values in the enum.
class Countries(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244


for country in Countries:
    print(country.name, "=", country.value)
