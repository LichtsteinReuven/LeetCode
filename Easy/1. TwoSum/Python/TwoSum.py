"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""


# The solution uses a dict which implements hash map.
# It is done so the complexity will be O(n) (amortized)
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {}
    for i, n in enumerate(nums):
        if (target - n) in nums_dict:
            return [nums_dict[target - n], i]
        nums_dict[n] = i
