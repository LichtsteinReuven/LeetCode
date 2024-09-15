"""
Given a m * n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -23^1 <= matrix[i][j] <= 23^1 - 1
"""


def set_row_and_col(matrix, row, col, val):
    """
    :type matrix: List[List[int]]
    :type row: int
    :type col: int
    :type val: int
    :rtype: None
    """
    for j in range(len(matrix[0])):
        if matrix[row][j] != 0:
            matrix[row][j] = val
    for i in range(len(matrix)):
        if matrix[i][col] != 0:
            matrix[i][col] = val


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    unique_val = 2 ** 31 + 5
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = unique_val
                set_row_and_col(matrix, i, j, unique_val)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == unique_val:
                matrix[i][j] =0
