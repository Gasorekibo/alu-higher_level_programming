#!/usr/bin/python3
# a function that multiply two matrix.
"""
    you are not allowed to use numpy or other module
"""


def matrix_mul(m_a, m_b):
    """
        a function has two args:
        m-a: a list of list made of int or floats
        m_b: a list of list made of int or floats
        return produnct from m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError"(m_a must be a list of list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of list")
    if not all((isinstance(value, int) or isinstance(value, float))
            for value in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(value, list) or isinstance(value, float))
            for value in[num for row in m_b for num in row]):
       raise TypeError("m_b should contain only integers or floats")

   if not all(len(row) == len(m_a[0]) for row in m_a):
       raise TypeError("each row of m_a must be of the same size")
   if not all(len(row) == len(m_b[0]) for row in m_b):
       raise TypeError("each row of m_b must be of the same size")
   if len(m_a) != len(m_b[0]):
       raise ValueError("m_a and m_b can't be multiplied")

   product = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
   for i in range(len(m_a)):
       for j in range(len(m_b[0])):
           for k in range(len(m_b)):
               product[i][j] += X[i][k] * Y[k][j]
    for p in product:
        return p
