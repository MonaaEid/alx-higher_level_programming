#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if type(my_list_1[i]) not in (int, float) or
                type(my_list_2[i]) not in (int, float):
                    print("wrong type")
                    result.append(0)
                elif my_list_2[i] == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(my_list_1[i] / my_list_2[i])
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
