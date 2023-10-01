#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be a list of lists")
    if not all(len(row) > 0 for row in m_a) or not all(len(row) > 0 for row in m_b):
        raise ValueError("m_a and m_b can't be empty")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a and each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(np.array(m_a), np.array(m_b)).tolist()

