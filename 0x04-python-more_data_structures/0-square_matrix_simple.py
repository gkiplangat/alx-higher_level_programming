#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix

    new_matrix = [square_array(x.copy()) for x in matrix]
    # new_matrix = list(map(square_array, matrix.copy()))
    return new_matrix


def square_array(array):
    return [i**2 for i in array]
