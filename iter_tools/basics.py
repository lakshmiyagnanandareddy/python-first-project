import itertools
# count - it will give us the infinite numbers in the iterable.
import operator

count = itertools.count()
"""
for i in count:
    print(i)
"""
print(next(count))
print(next(count))
# zip - we can make pairs
data = [10, 29, 44, 33, 22]
daily_data = zip(itertools.count(), data)
print(list(daily_data))

count = itertools.count(start=4, step=2)
print(next(count))
print(next(count))
print(next(count))

Names = ["Nandu", "Vignesh", "Vinitha", "Sudharshan"]
appointment_list = zip(range(10), Names)
print(list(appointment_list))
appointment_list = itertools.zip_longest(range(10), Names)
print(list(appointment_list))

count = itertools.cycle(['on', 'off'])
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))

count = itertools.repeat(['on', 'off'], times=5)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))

count = map(pow, range(10), itertools.repeat(2))
print(list(count))

count = itertools.starmap(pow, [(9, 2), (4, 2), (6, 7)])
print(list(count))

numbers = [0, 1, 2, 3]
print(list(itertools.combinations(numbers, 2)))

print(list(itertools.permutations(numbers, 2)))
print(list(itertools.combinations_with_replacement(numbers, 2)))

alphabets = ['A', 'B', 'C', 'D']
print(list(itertools.chain(numbers, alphabets)))

# print(list(itertools.islice(range(10), start=2, stop=6, step=3)))
print(list(itertools.islice(range(10), 2, 6, 3)))

validate = [True, True, False, True]
print(list(itertools.compress(alphabets, validate)))


def condition(num):
    if num < 2:
        return True
    return False


numbers = [1, 2, 3, 2, 1, 0, 1]
print(list(filter(condition, numbers)))
print()
print(list(itertools.filterfalse(condition, numbers)))

# dropwhile - will check until the condition true, if once the condition is true, it not check the condition for next values.
print(list(itertools.dropwhile(lambda x: x < 2, numbers)))

# takewhile - will work until the condition true, if once the condition is true, it will not move forward.
print(list(itertools.takewhile(lambda x: x < 2, numbers)))

print(list(itertools.accumulate(numbers)))
print(list(itertools.accumulate(numbers, operator.mul)))


names_in_the_city = [
    {
        'Name': 'Nandu',
        'city': 'jaipur',
        'job': 'student'
    },
    {
        'name': 'Reddy',
        'city': 'Andhra',
        'job': 'farmer'
    },
    {
        'name': 'Vinitha',
        'city': 'Andhra',
        'job': 'student'
    },
    {
        'name': 'sudharsan',
        'city': 'proddatur',
        'job': 'bussines'
    },
]
def get_state(names):
    return names['city']
people = itertools.groupby(names_in_the_city,get_state)
for key, group in people:
    print(key, list(group))
