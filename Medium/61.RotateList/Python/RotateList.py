"""
Given the head of a linked list, rotate the list to the right by k places.


Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        length = 0
        ptr = head
        tail = None
        while ptr:
            length += 1
            if not ptr.next:
                tail = ptr
            ptr = ptr.next
        k %= length
        if k == 0:
            return head
        tail.next = head
        for i in range(length - k):
            temp = head
            head = head.next
            if i == length - k - 1:
                temp.next = None
        return head