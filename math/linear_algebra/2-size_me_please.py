#!/usr/bin/env python3
"""Module that calculates the shape of a matrix."""


def matrix_shape(matrix):
    """Returns the shape of a matrix as a list."""
    dimensions = []

    while isinstance(matrix, list):
        dimensions.append(len(matrix))
        matrix = matrix[0]

    return dimensions
