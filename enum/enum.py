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
print(apples[Color(1)])

print(Color.RED.value)

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

"""
from enum import Enum, unique


@unique
class numbers(Enum):    # "@unique" - it will take duplicate values, and it will raise type error.
    one = 5
    two = 8
    three = 9
    four = 9


for number in numbers:
    print(number)
"""
from enum import Enum, auto


class auto_colors(Enum):
    RED = auto()    # "auto()" - it will take a values from 1 automatically.
    GREEN = auto()
    YELLOW = auto()


print(list(auto_colors))


class Autonumber(Enum):
    def _generate_next_value_(self, start, count, last_values):     # it will return  the same Enum member as a value.
        return self


class name(Enum):
    purple = auto()
    brown = auto()


class second_name(Autonumber):
    blue = auto()
    grey = auto()


print(list(name))
print(list(second_name))


class Mood(Enum):
    FUNKY = 1
    HAPPY = 4

    def describe(self):
        return self.name, self.value

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY

    def __str__(self):
        return format(self.value)


print(Mood.describe(Mood.FUNKY))
print(str(Mood.FUNKY))
print(Mood.favorite_mood())

"""
from test.test_enum import Fruit
from pickle import dumps,loads
print(Fruit.Tomato is loads(dumps(Fruit.Tomato)))
"""

Animal = Enum("animal", "LION CAT DOG TIGER")
print("Animal :", Animal)
print("Animal.TIGER :", Animal.TIGER)
print("Animal.Tiger.name :", Animal.TIGER.name)
print("Animal.Tiger.value :", Animal.TIGER.value)
print("list(Animal)", list(Animal))


from enum import IntEnum


class ice(IntEnum):
    vanilla = 1
    butter_scotch = 5
    choclate = 3


class animal_in_IntEnum(IntEnum):
    goat = 5
    lion = 1
    tiger = 3


class animal_in_Enum(Enum):
    goat = 5
    lion = 1
    tiger = 3


print("ice.vanilla == Animal_in_IntEnum.lion :", ice.vanilla == animal_in_IntEnum.lion)

print("ice.vanilla == Animal_in_IntEnum.lion :", ice.vanilla == animal_in_Enum.lion)

from enum import IntFlag


class prem(IntFlag):    # enum"IntFlag is will combine the values"
    R = 4
    W = 2
    T = 3


print("(prem.R|prem.W|prem.T).value =", (prem.R | prem.W | prem.T).value)
print((prem.R ^ prem.T).value)
print("repr(prem.R) =", repr(prem.R))
print("~prem.R.value =", ~prem.R.value)

print(prem.R & prem.T)

print()


class Coordinate(bytes, Enum):
    def __new__(cls, value, label, unit):
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label
        obj.unit = unit
        return obj

    PX = (0, "p.x", "km")
    PY = (7, "p.y", "ab")
    PZ = (2, "p.z", "ABc")


print(Coordinate["PX"])
print(Coordinate["PX"].value)
print(Coordinate["PY"].unit)
print(Coordinate["Abc"])


class color_obj(Enum):
    RE = object()
    GREEN = object()
    YELLOW = object()


print(color_obj.RE)
