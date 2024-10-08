"""
You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search_row(matrix, target, 0, len(matrix) - 1)

    def search_row(self, matrix, target, start_idx, end_idx):
        if start_idx > end_idx:
            return False
        middle = (start_idx + end_idx) // 2
        row = matrix[middle]
        if row[0] <= target <= row[- 1]:
            return self.search_col(row, target, 0, len(matrix[middle]) - 1)
        if row[0] > target:
            return self.search_row(matrix, target, start_idx, middle - 1)

        return self.search_row(matrix, target, middle + 1, end_idx)

    def search_col(self, col, target, start_idx, end_idx):
        if start_idx > end_idx:
            return False
        middle = (start_idx + end_idx) // 2
        if col[middle] == target:
            return True
        if col[middle] > target:
            return self.search_col(col, target, start_idx, middle - 1)

        return self.search_col(col, target, middle + 1, end_idx)


sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))  # True
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1))  # True
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34))  # True
