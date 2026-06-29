#!/usr/bin/env python3
"""Module that calculates the determinant of a matrix."""


def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): Matrix whose determinant is calculated.

    Returns:
        int or float: Determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    """

    # Check if matrix is a list of lists
    if (not isinstance(matrix, list) or
            len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    # Special case for 0x0 matrix
    if matrix == [[]]:
        return 1

    n = len(matrix)

    # Check if matrix is square
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive Laplace expansion along the first row
    det = 0
    for col in range(n):
        # Build the minor matrix
        minor = []
        for row in matrix[1:]:
            minor.append(row[:col] + row[col + 1:])

        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det
