"""
1.8 - Zero Matrix: Write an algorithm such that if an element in 
an M x N matrix is 0, its entire row and column are set to 0.

Time Complexity: O(n*m)
Space Complexity: O(n)

This could also be done in O(1) space complexity by passing over the entire matrix twice.
Instead of saving if the row and col need to be zeroed, set that row and col to None right
away. On the second pass, set all None to 0.

Author: Jonah Beers
"""

matrix = [[0, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], 
           [5, 0, 7, 8],
           [9, 8, 0, 6],
           [5, 4, 3, 2]]

def zero_matrix(mat):
    rows = [False for i in range(len(mat))]
    cols = [False for j in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(len(rows)):
        if rows[i]: 
            zero_row(mat, i)
    for j in range(len(cols)):
        if cols[j]:
            zero_col(mat, j)

def zero_row(mat, row):
    for j in range(len(mat[0])):
        mat[row][j] = 0

def zero_col(mat, col):
    for i in range(len(mat)):
        mat[i][col] = 0
        
def print_matrix(mat):
    for i in range(len(mat)):
        print('| ', end='')
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print('|\n', end='')
        
def show_zeroed_matrix(mat):
    print('Matrix before zeroing:')
    print_matrix(mat)
    zero_matrix(mat)
    print('\nMatrix after zeroing:')
    print_matrix(mat)
        
# Driver
show_zeroed_matrix(matrix)
print()
show_zeroed_matrix(matrix2)