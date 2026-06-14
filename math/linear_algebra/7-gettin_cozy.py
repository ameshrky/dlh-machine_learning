#!/usr/bin/env python3
"""Module that concatenates two 2D matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a specific axis."""

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None

        new_matrix = []

        for row in mat1:
            new_matrix.append(row.copy())

        for row in mat2:
            new_matrix.append(row.copy())

        return new_matrix

    if axis == 1:
        if len(mat1) != len(mat2):
            return None

        new_matrix = []

        for i in range(len(mat1)):
            new_row = mat1[i].copy() + mat2[i].copy()
            new_matrix.append(new_row)

        return new_matrix

    return None
