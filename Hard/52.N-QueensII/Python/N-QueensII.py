"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.


Example 1:
    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 9
"""

class Solution:

    def __init__(self):
        self.n = None
        self.placement_counter = None
        self.queens_x = None
        self.queens_y = None

    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.placement_counter = 0
        self.queens_x = []
        self.queens_y = []
        self._total_queens_helper(0)
        return self.placement_counter

    def _total_queens_helper(self, row):
        if row == self.n:
            self.placement_counter += 1
        for col in range(self.n):
            if self._is_valid(row, col):
                self.queens_x.append(row)
                self.queens_y.append(col)
                self._total_queens_helper(row + 1)
                self.queens_x.pop()
                self.queens_y.pop()

    def _is_valid(self, row, col):
        if row in self.queens_x or col in self.queens_y:
            return False
        for i in range(len(self.queens_x)):
            if ((row + col == self.queens_x[i] + self.queens_y[i]) or
                    (row - col == self.queens_x[i] - self.queens_y[i])):
                return False
        return True