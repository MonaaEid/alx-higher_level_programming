#!/usr/bin/python3
def print_matrix_intger(matrix=[[]]):
    for row in matrix:
        row_string = ""
        for i in range(len(row)):
            row_string += "{:d}".format(row[i])
            if i < len(row) - 1:
                row_string += " "
        print(row_string)
