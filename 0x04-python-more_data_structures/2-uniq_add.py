#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    sum = 0
    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)
            sum += i
    return sum
