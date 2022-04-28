"""
Write a Python program that can suspend execution of a given script a given number of seconds.
Sample Output:
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...
Sorry, Slept for 3 seconds...
"""
import time
i = 2
time.sleep(3)
print("sorry, slept for 3 seconds...")
while i > 0:
    time.sleep(3)
    print("sorry, slept for 3 seconds...")
    print("while")

