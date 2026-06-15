#!/usr/bin/env python3
"""Module that adds arrays element-wise."""

import numpy as np

def np_cat(mat1, mat2, axis=0):
    """Returns the element-wise addition of two arrays."""

    return np.concatenate((mat1, mat2), axis=axis)
