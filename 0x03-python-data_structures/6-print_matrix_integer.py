#!/usr/bin/python3
def print_matrix_intger(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(n) for n in row))
