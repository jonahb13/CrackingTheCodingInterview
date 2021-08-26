"""
1.7 - Rotate Matrix: Given an image represented by an N x N matrix, where each 
pixel in the image is represented by an integer, write a method to rotate the 
image by 90 degrees. Can you do this in place?

Time Complexity: O(n^2)
Space Complexity: O(1)

Author: Jonah Beers
"""

matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], 
           [5, 6, 7, 8],
           [9, 8, 7, 6],
           [5, 4, 3, 2]]

def rotate_matrix(mat):
    length = len(mat)
    if length == 0 or length != len(mat[0]): 
        return
    for row in range(length//2):
        first = row
        last = length - 1 - row
        for i in range(first, last):
            offset = i - first
            top = mat[first][i]
            mat[first][i] = mat[last-offset][first]
            mat[last-offset][first] = mat[last][last-offset]
            mat[last][last-offset] = mat[i][last]
            mat[i][last] = top
            
def print_matrix(mat):
    for i in range(len(mat)):
        print('| ', end='')
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print('|\n', end='')
        
def show_rotation(mat):
    print('Matrix before rotation:')
    print_matrix(mat)
    rotate_matrix(mat)
    print('\nMatrix after rotation:')
    print_matrix(mat)
            
# Driver
show_rotation(matrix)
print()
show_rotation(matrix2)
