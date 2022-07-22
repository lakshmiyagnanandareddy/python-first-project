"""
 Write a Python program to generate an infinite cycle of elements from an iterable.
"""
import itertools
infinte_cycle = itertools.cycle(itertools.count())
for cycle in infinte_cycle:
    print(cycle)