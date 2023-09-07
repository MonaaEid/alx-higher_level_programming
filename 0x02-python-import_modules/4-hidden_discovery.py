#!/usr/bin/python3
import importlib
hidden_4 = importlib.import_module("hidden_4")
def main():
    names = dir(hidden_4)

    names = sorted(names)

    for name in names:
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()
