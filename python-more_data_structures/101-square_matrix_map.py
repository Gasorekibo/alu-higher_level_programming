#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    for i in matrix:
        new = list(map(lambda num : (num ** 2), i))
        return new
