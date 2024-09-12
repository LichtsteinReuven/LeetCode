"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, the output is 1 and 2.

Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore, the output is 1 and 3.

Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore, the output is 1 and 2.

Constraints:
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
"""


def binary_search(array, start, end, target):
    """
    :type array: List[int]
    :type start: int
    :type end: int
    :type target: int
    :rtype: int
    """
    middle = (end + start) // 2
    if start > end:
        return -1
    if array[middle] == target:
        return middle
    if target > array[middle]:
        return binary_search(array, middle + 1, end, target)
    else:
        return binary_search(array, start, middle - 1, target)


def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(numbers)
    for i in range(length):
        idx = binary_search(numbers, i + 1, length - 1, target - numbers[i])
        if idx != -1:
            return [i + 1, idx + 1]
