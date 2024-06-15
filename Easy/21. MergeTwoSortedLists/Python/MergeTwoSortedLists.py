"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Base cases: if either list is empty, return the other list
    if list1 == None:
        return list2
    if list2 == None:
        return list1

    # Recursive case: if the value of list1 is less than list2,
    # set the next node of list1 to the result of the recursive call
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    # Otherwise, set the next node of list2 to the result of the recursive call
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2