#!/usr/bin/python3

for x in reversed(range(97, 123)):
    counter = x
    if counter % 2 != 0:
        counter -= 32
    print("{}".format(chr(counter)), end="")
