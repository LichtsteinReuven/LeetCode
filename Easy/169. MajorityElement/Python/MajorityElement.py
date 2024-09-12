"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
    Input: [3,2,3]
    Output: 3

Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    - n == nums.length
    - 1 <= nums.length <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9
"""

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums) / 2
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = nums.count(num)
    for key, value in counts.items():
        if value > n:
            return key
