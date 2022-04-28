from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


# Color.RED = 6


print(Color.RED.name)  # .name - it will give item name.
print(Color.GREEN.value)  # .value - it will give assigned value.
print(repr(Color.RED))  # repr - will give the information of that name.
print(type(Color.RED))  # type() - it will gives the red is belongs too.
print(isinstance(Color.RED, Color))


class Shakes(Enum):
    vinila = 20
    chacobar = 30
    mango = 30
    lemon = 40


for shake in Shakes:
    print(shake)  # Enum is iterable, doesn't allow same, but not same enum_members values.

apples = {}
apples[Color.RED] = "abc"
apples[Color.GREEN] = 20
print(apples)
print(Color.RED.value)
print(apples[Color.RED])
print(Color(1))
print(Color["RED"])

"""
class duplicating(Enum):
    Vignesh = 18
    Vignesh = 30
    Nandu = 20


try:
    print(duplicating)  # it will raises the "type error" because it doesn't allows Enum duplicate numbers.
except:
    print("Type error")
"""

from enum import Enum, unique


@unique
class numbers(Enum):
    one = 5
    two = 8
    three = 9
    four = 9


for number in numbers:
    print(number)