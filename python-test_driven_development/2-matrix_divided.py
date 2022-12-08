#!/usr/bin/python3
# a function that divides all elements of a matrix
"""
    we are going to divide a matrix list of element
"""


def matrix_divided(matrix, div):
    """
        argument:
            matrix: a list of integer and div which is the element to be 
            divided to the matrix
    """
    new_matrix = []
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(value, int) or isinstance(value, float))
            for value in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix (list of lists) of "
                    "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    else:
        for i in matrix:
            result = list(map(lambda x : round(x/div, 2), i))
            new_matrix.append(result)
        return(new_matrix)
