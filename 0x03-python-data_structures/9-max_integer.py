#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximum = my_list[0]
    for num in my_list[1:]:
        if num > maximum:
            maximum = num
    return maximum
