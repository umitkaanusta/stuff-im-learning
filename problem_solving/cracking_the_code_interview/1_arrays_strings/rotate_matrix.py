"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

# further ask: just to clarify, i'll be using python, would
#       that 4-bytes change something for me (how should i represent pixels)

"""
Let's come up with an instance

a b c d e f             5 y s m g a
g h i j k l             6 z t n h b
m n o p q r    ------>  7 1 u o i c
s t u v w x             8 2 v p j d
y z 1 2 3 4             9 3 w q k e
5 6 7 8 9 0             0 4 x r l f

row 0 becomes col 5
row 1 -> col 4 and so on..
"""
from math import ceil


def rotate_nxn_matrix_90deg(matrix):
    # O(n^2) time, not in-place
    rotated_mtx = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for row_idx in range(len(matrix)):
        rotated_col_idx = len(matrix) - 1 - row_idx
        for col_idx in range(len(matrix)):
            rotated_row_idx = col_idx
            rotated_mtx[rotated_row_idx][rotated_col_idx] = matrix[row_idx][col_idx]
    return rotated_mtx


def rotate_nxn_matrix_90deg_inplace(matrix):
    # circular rotation, start from the outermost layer
    for layer in range(ceil(len(matrix) / 2)):
        first = layer
        last = len(matrix) - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # save top
            matrix[first][i] = matrix[last - offset][first]  # top = left
            matrix[last - offset][first] = matrix[last][last - offset]  # left = bottom
            matrix[last][last - offset] = matrix[i][last]  # bottom = right
            matrix[i][last] = top  # right = top
    return matrix


def test_solution():
    mtx = [
        ["a", "b", "c", "d", "e", "f"],
        ["g", "h", "i", "j", "k", "l"],
        ["m", "n", "o", "p", "q", "r"],
        ["s", "t", "u", "v", "w", "x"],
        ["y", "z", "1", "2", "3", "4"],
        ["5", "6", "7", "8", "9", "0"]
    ]
    rotated_mtx = [
        ["5", "y", "s", "m", "g", "a"],
        ["6", "z", "t", "n", "h", "b"],
        ["7", "1", "u", "o", "i", "c"],
        ["8", "2", "v", "p", "j", "d"],
        ["9", "3", "w", "q", "k", "e"],
        ["0", "4", "x", "r", "l", "f"]
    ]
    assert rotate_nxn_matrix_90deg(mtx) == rotated_mtx
    assert rotate_nxn_matrix_90deg_inplace(mtx) == rotated_mtx


if __name__ == '__main__':
    test_solution()
