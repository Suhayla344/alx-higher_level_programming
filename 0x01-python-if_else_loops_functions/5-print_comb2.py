#!/usr/bin/python3
for x in range(100):
    if x == 99:
        print(x)
    else:
        print("{:02}".format(x), end=", ")
