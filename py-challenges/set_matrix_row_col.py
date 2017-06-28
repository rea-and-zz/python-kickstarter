import random
import copy


def set_matrix_row_col_to_num(matrix, row, col, num):
    # First let's set the whole column
    for i in range(0, len(matrix)):
        matrix[i][col] = num

    # Then le'ts set the row
    for i in range(0, len(matrix[0])):
        matrix[row][i] = num

def transform_matrix(matrix , num):
    matrix_tmp = copy.deepcopy(matrix)

    for index_r, row in enumerate(matrix):
        for index_c, item in enumerate(matrix[index_r]):
            if item == num:
                set_matrix_row_col_to_num(matrix_tmp, index_r, index_c, num)

    # Matrix fully scanned, replace the original matrix with the tmp one
    return matrix_tmp

sample = [[3, 1, 7 ,9],
          [5, 7, 7, 3],
          [1, 4, 7 ,9],
          [5, 7, 7, 3],
          [5, 7, 8, 4]]


print("\n\nInput:")
for row in sample:
    print(row)

print("Processing now...")
new_sample = transform_matrix(sample, 1)

print("Done! Result:")
for row in new_sample:
    print(row)





rows = 10
columns = 10
matrix = [[x for x in range(columns)] for y in range(rows)]

