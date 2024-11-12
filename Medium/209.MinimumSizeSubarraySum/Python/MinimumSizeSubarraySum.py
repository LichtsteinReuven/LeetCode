"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

Constraints:
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        nums_sum = sum(nums)
        if nums_sum < target:
            return 0

        length = len(nums)
        if nums_sum == target:
            return length

        nums_max = max(nums)
        if nums_max >= target:
            return 1

        min_length = length

        start = end = 0
        current_sum = nums[start]

        while start < length:
            if (start == end or current_sum < target) and end + 1 < length:
                end += 1
                current_sum += nums[end]
            if current_sum >= target:
                if (end - start + 1) < min_length:
                    min_length = end - start + 1
            if current_sum >= target:
                current_sum -= nums[start]
                start += 1
            if min_length == 1 or (end == length - 1 and current_sum < target):
                break

        return min_length
