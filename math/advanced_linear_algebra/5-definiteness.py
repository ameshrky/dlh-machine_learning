#!/usr/bin/env python3
"""Module that determines the definiteness of a matrix."""

import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix."""

    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if (matrix.ndim != 2 or
            matrix.shape[0] != matrix.shape[1] or
            matrix.size == 0):
        return None

    # Definiteness is only defined for symmetric matrices
    if not np.array_equal(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)

    eps = 1e-8

    if np.all(eigenvalues > eps):
        return "Positive definite"

    if np.all(eigenvalues >= -eps):
        return "Positive semi-definite"

    if np.all(eigenvalues < -eps):
        return "Negative definite"

    if np.all(eigenvalues <= eps):
        return "Negative semi-definite"

    if np.any(eigenvalues > eps) and np.any(eigenvalues < -eps):
        return "Indefinite"

    return None
