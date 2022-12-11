#!/usr/bin/python3
# a function that maltiply two matrices
"""
    wea re not allowed to import any module
"""


def matrix_mul(m_a, m_b):
    """
        args:
            m_a: a list of list made of int or float(matrix 1)
            m_b: a list of list made of int or float(matrix 2)
        return :
        product from m_a * m_b
    """
    product = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        product.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in product:
            prod = 0
            for i in range(len(product[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)
    return new_matrix
