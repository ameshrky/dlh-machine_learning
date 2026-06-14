#!/usr/bin/env python3
"""Module that multiplies two matrices."""


def mat_mul(mat1, mat2):
    """Multiply two matrices."""

    if len(mat1[0]) != len(mat2):
        return None

    new_matrix = []

    for row in mat1:
        new_row = []

        for col in range(len(mat2[0])):
            total = 0

            for i in range(len(mat2)):
                total += row[i] * mat2[i][col]

            new_row.append(total)

        new_matrix.append(new_row)

    return new_matrix
