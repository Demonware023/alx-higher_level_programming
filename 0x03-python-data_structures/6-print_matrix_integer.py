#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            if num != len(matrix[row]) - 1:
                endspace = ' '
            else:
                endspace = ''
            print("{:d}".format(matrix[row][num]), end=endspace)
        print()
