#!/usr/bin/env python3
"""Module that transposes a matrix."""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix."""

    rows_len = len(matrix)
    columns_len = len(matrix[0])

    new_matrix = []

    for c in range(columns_len):
        new_row = []
        for r in range(rows_len):
            new_row.append(matrix[r][c])
        new_matrix.append(new_row)

    return new_matrix
