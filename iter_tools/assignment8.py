"""
Write a Python program to split an iterable and generate iterables specified number of times.
"""
import itertools
word = "My name is Nandu"
generated_iters = itertools.tee(word, 5)
for iters in generated_iters:
    print(list(iters))