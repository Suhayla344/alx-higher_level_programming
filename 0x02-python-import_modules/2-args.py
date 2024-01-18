#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    size = len(argv)
    if size == 1:
        print("0 arguments.")
    elif size == 2:
        print("{} argument:".format(size - 1))
    else:
        print("{} arguments:".format(size - 1))

    for ind in range(1, len(argv)):
        print("{}: {}".format(ind, argv[ind]))
