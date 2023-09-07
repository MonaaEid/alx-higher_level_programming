#!/usr/bin/python3
import sys
def main():
    num_args = len(sys.argv)

    if num_args == 1:
        print("Number of argument: 0.")
    elif num_args == 2:
        print("Number of argument: 1:")
    else:
        print("Number of arguments: {}:".format(num_args - 1))

    for i in range(1, num_args):
        print("{}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    main()
