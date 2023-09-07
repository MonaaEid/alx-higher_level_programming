#!/usr/bin/python3
import sys
argv = sys.argv

if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))
    for i in range(1, num + 1):
        print("{}: {}".format(i, argv[i]))
