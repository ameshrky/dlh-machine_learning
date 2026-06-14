#!/usr/bin/env python3
"""Module that transposes a matrix."""


def add_matrices2D(mat1, mat2):
    """Returns the transpose of a 2D matrix."""

    mat1_rows = len(mat1)
    mat2_rows = len(mat2)
    mat1_cols = len(mat1[0])
    mat2_cols = len(mat2[0])

    if mat1_cols != mat2_cols or mat1_rows != mat2_rows:
        return None

    new_matrix = []

    for r in range(mat1_rows):
        new_row = []
        for c in range(mat1_cols):
            new_row.append(mat1[r][c] + mat2[r][c])
        new_matrix.append(new_row)

    return new_matrix
