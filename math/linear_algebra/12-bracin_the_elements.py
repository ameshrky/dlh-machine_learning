#!/usr/bin/env python3
"""Module that adds arrays element-wise."""


def np_elementwise(mat1, mat2):
    """Returns the element-wise addition of two arrays."""

    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2

    return add, sub, mul, div
