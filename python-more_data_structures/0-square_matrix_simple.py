#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [squares ** 2 for i in matrix for squares in i]
    print(new_matrix)
