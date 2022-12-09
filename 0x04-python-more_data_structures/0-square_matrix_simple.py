#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Create a new empty matrix with the same size as the input matrix

    squared_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]



    # Iterate over each element in the input matrix

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            # Compute the square of the element and store it in the new matrix

            squared_matrix[i][j] = matrix[i][j] ** 2



    # Return the new squared matrix

    return squared_matrix
