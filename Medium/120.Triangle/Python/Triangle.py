"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally,
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
       2
      3 4
     6 5 7
    4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
    Input: triangle = [[-10]]
    Output: -10

Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        path_min = []

        if rows == 1:
            return triangle[0][0]

        for row in range(rows):
            path_min.append([0] * (row + 1))

        path_min[0][0] = triangle[0][0]

        last_row_min = float('inf')

        for row in range(1, rows):
            for col in range(row + 1):

                left = right = float('inf')
                val = triangle[row][col]

                if col != 0:
                    left = path_min[row - 1][col - 1] + val
                if col != row:
                    right = path_min[row - 1][col] + val

                path_min[row][col] = min(left, right)

                if row == rows - 1:
                    if path_min[row][col] < last_row_min:
                        last_row_min = path_min[row][col]

        return last_row_min
