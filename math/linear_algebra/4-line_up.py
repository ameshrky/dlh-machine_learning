#!/usr/bin/env python3
"""Module that transposes a matrix."""


def add_arrays(arr1, arr2):
    """Returns the transpose of a 2D matrix."""

    arr1_len = len(arr1)
    arr2_len = len(arr2)

    if arr1_len != arr2_len:
        return None
    
    new_array = []

    for c in range(arr1_len):
            new_array.append(arr1[c] + arr2[c])
    
    return new_array
