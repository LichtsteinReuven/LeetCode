"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self._helper(nums, target, 0, len(nums) - 1)

    def _helper(self, nums, target, start_idx, end_idx):
        if start_idx >= end_idx:
            if nums[start_idx] == target:
                return start_idx
            if nums[start_idx] < target:
                return start_idx + 1
            return start_idx
        middle = (start_idx + end_idx) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            return self._helper(nums, target, middle + 1, end_idx)
        else:
            return self._helper(nums, target, start_idx, middle - 1)
