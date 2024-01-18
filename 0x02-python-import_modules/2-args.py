#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    size = len(sys.argv)
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("{} argument:".format(size - 1))
    else:
        print("{} arguments:".format(size - 1))

    for ind in range(1, len(argv)):
        print("{}: {}".format(ind, argv[ind]))
