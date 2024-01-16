#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10
print("Last digit of", end=" ")
if x > 5:
    print("{} is {} and is greater than 5".format(number, x))
elif x == 0:
    print("{} is {} and is 0".format(number, x))
else:
    print("{} is {} and is less than 6 and not 0".format(number, x))
