#!/usr/bin/python3
"""
This is the "lazy matrix multiplication" module
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices by using the module NumPy
    Args:
        m_a: list of integers or floats
        m_b: list of integers or floats
    """
    return (np.matmul(m_a, m_b))
