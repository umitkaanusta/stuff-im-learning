"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0. Do not set the newly-added zeros' columns and rows to 0.
"""

"""
Creating a handmade example:

1, 2, 0,        0, 0, 0
4, 5, 6,   ---> 4, 5, 0,
7, 9, 2         7, 9, 0
"""


def make_row_col_zero(matrix):
    # O(mn) time
    nullify_rows = {}
    nullify_cols = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                nullify_rows[i] = True
                nullify_cols[j] = True
    # make all rows involving zeros, zero
    for row_idx in nullify_rows:
        for col_idx in range(len(matrix)):
            matrix[row_idx][col_idx] = 0
    # make all cols involving zeros, zero
    for col_idx in nullify_cols:
        for row_idx in range(len(matrix)):
            matrix[row_idx][col_idx] = 0
    return matrix


def make_row_col_zero_space_optimized(matrix):
    # O(m^2 + n^2) time, O(1) space
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                # make row None
                for col_idx in range(len(matrix[0])):
                    matrix[i][col_idx] = None
                # make col None
                for row_idx in range(len(matrix)):
                    matrix[row_idx][j] = None
            print(matrix)
    # now make all None's zero, we do this to not confuse newly added zeros with existing zeros
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is None:
                matrix[i][j] = 0
    return matrix


# we can come up w/ an algorithm with O(mn) time and O(1) space, look at the book for that

def test_solution():
    mtx = [
        [1, 2, 0],
        [4, 5, 6],
        [7, 9, 2]
    ]
    zeroed_mtx = [
        [0, 0, 0],
        [4, 5, 0],
        [7, 9, 0]
    ]
    assert make_row_col_zero(mtx) == zeroed_mtx

    mtx = [
        [1, 2, 0],
        [4, 5, 6],
        [7, 9, 2]
    ]
    zeroed_mtx = [
        [0, 0, 0],
        [4, 5, 0],
        [7, 9, 0]
    ]
    assert make_row_col_zero_space_optimized(mtx) == zeroed_mtx


if __name__ == '__main__':
    test_solution()
