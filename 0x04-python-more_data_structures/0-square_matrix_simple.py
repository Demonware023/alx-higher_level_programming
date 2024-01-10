#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        square = map(lambda x: x ** 2, matrix[row])
        new_matrix.append(list(square))
    return (new_matrix)
