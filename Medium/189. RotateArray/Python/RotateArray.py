"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation:
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
    1 <= nums.length <= 10^5
    -231 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5
"""


def reverse(nums, start, end):
    """
    :type nums: List[int]
    :type start: int
    :type end: int
    :rtype: None
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    k %= length
    if k == 0:
        return
    reverse(nums, 0, length - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, length - 1)