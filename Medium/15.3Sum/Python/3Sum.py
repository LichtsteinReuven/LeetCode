"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
                 nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
                 nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
                 The distinct triplets are [-1,0,1] and [-1,-1,2].
                 Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0, 1, 1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0, 0, 0]
    Output: [[0, 0, 0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums_len = len(nums)
    sorted_nums = sorted(nums)
    output = set()
    for i in range(nums_len - 1):
        if i != 0 and sorted_nums[i - 1] == sorted_nums[i]:
            continue
        target = -sorted_nums[i]
        start = i + 1
        end = nums_len - 1
        while start < end:
            two_sum = sorted_nums[start] + sorted_nums[end]
            if two_sum == target:
                output.add((sorted_nums[i], sorted_nums[start], sorted_nums[end]))
                start += 1
                end -= 1
            elif two_sum > target:
                end -= 1
            else:
                start += 1
    output = [list(item) for item in output]
    return output
