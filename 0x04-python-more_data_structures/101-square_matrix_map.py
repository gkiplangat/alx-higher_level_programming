#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda m: list(map(lambda n: n**2, m)), matrix.copy()))
