"""
You are given an integer array height of length n. There are n vertical  lines drawn such that the two
endpoints of the ith line are (i, 0) and (i, height[i]).

Find the two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
                 In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4
"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_amount = float('-inf')
    start = 0
    end = len(height) - 1
    while start < end:
        amount = (end - start) * min(height[start], height[end])
        if amount > max_amount:
            max_amount = amount
        if height[start] <= height[end]:
            start += 1
        else:
            end -= 1
    return max_amount
