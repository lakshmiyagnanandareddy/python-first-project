"""
Write a Python program to create an iterator from several iterables in a sequence and
display the type and elements of the new iterator.
"""
import itertools
alphabets = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 5]
iterator = itertools.chain(alphabets, numbers)
for create_iter in iterator:
    print(create_iter)