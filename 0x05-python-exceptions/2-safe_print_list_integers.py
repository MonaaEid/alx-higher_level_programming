#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end='')
        except ValueError:
            pass
        except TypeError:
            pass
        else:
            count += 1
        print()
        return (count)
