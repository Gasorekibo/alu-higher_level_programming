#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = []
    new.append(list(map(lambda num: (num**2), matrix[0])))
    new.append(list(map(lambda num: (num**2), matrix[1])))
    new.append(list(map(lambda num: (num**2), matrix[2])))
    print(new)
