"""
Given a sorted array nums, remove the duplicates in-place
such that duplicates appeared at most twice and return the new length.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2,
    with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
    Input: nums = [0,0,1,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5,
    with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
"""


def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = k = 0
    flag = False

    for i, num in enumerate(nums):
        if i != 0 and num == prev:
            if (not flag):
                flag = True
                j = i
        else:
            k += 1
            if (flag):
                nums[j] = num
                j += 1
        prev = num
    return k
