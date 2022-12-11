#!/usr/bin/python3
"""
    multiplying two matrix using python Numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        argument: m_a which is matrix
                  m_b which is also a matrix 
                  this return m_a * m_b
    """
    return (np.matmul(m_a, m_b))
