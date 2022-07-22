from __future__ import print_function
import __future__
print(__future__.all_feature_names)
"""
__future__: is to to use the old versions futures 
['nested_scopes',
 'generators',
 'division',
 'absolute_import',
 'with_statement',
 'print_function',
 'unicode_literals',
 'barry_as_FLUFL',
 'generator_stop',
 'annotations']
"""
"""
nested_scopes : In this the nested class are not allowed ex= main.sub_main
"""
"""
Generators:We are using a generator to randomly seed a sequence of specifications for the
    factory. While this is not strictly part of the Factory Pattern, it can be useful
    for testing the factory or for generating objects based on some pre-defined algorithm.
    It is perfectly acceptable to implement factories without generators (depends on your
    specific use-case).
"""
"""
division:Using division we will use "/".
"""
"""
absolute_import: in this we not able to use (* - to import all function in a module).
"""
"""
print_function: in print_function thier will not able to concatenation(, ), (end="") - with empty.
"""
"""
unicode_literals: we can convert a string into the universal character set(unicode).
"""
"""
barry_as_FLUFL: something that will not work (2 != 3) - for comparison, (2 <> 3) - will work 
"""
"""
generator_stop : if we use iterator, in this if we want to stop while running it raises runtime error.
"""

