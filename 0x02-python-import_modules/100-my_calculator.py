#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

import sys


def main():
    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]

    b = int(sys.argv[3])
    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }
    func = operations[operator]
    result = func(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
