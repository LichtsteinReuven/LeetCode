"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.


Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in a strictly increasing order.
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    return buildBST(nums, 0, len(nums) - 1)


def buildBST(nums: List[int], start: int, end: int) -> Optional[TreeNode]:
    if start > end:
        return None
    if start == end:
        return TreeNode(nums[start])
    middle = (start + end) // 2
    root = TreeNode(nums[middle])
    root.left = buildBST(nums, start, middle - 1)
    root.right = buildBST(nums, middle + 1, end)
    return root
