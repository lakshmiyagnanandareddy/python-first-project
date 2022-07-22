"""
 Write a Python program to find four elements from a given array of integers whose sum is equal to a given number.
 The solution set must not contain duplicate quadruplets. Go to the editor
Expected Output:
Array values & target value: [-2, -1, 1, 2, 3, 4, 5, 6] & 10
"""
import itertools
value = [-2, -1, 1, 2, 3, 4, 5, 6]
for quardruples in itertools.combinations(value, 4):
    if sum(quardruples) == 10:
        print(quardruples)