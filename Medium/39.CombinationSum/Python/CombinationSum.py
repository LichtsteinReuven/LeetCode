"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique
combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than
150 combinations for the given input.


Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Constraints:
    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40
"""


class Solution:

    def __init__(self):
        self._combinations = None
        self._candidates = None

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self._combinations = []

        self._candidates = candidates
        self._candidates.sort()
        self._combinations_helper(0, [], target)
        return self._combinations

    def _combinations_helper(self, index, current_combination, current_target):
        if current_target == 0:
            if current_combination not in self._combinations:
                self._combinations.append(current_combination.copy())
                return
        if current_target < 0:
            return
        for i in range(index, len(self._candidates)):
            candidate = self._candidates[i]
            if candidate > current_target:
                break
            current_combination.append(candidate)
            self._combinations_helper(i, current_combination, current_target - candidate)
            current_combination.pop()