"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


DECIMAL_BASE = 10


def sum_and_carry(num):
    """
    Returns the sum and the carry of the given number
    """
    return num % DECIMAL_BASE, num // DECIMAL_BASE


def add_end_of_list(lst, my_sum, carry):
    """
    Adds the remaining elements of the list to the sum
    :type lst: ListNode
    :type my_sum: ListNode
    :type carry: ListNode
    :rtype: ListNode
    """
    while lst:
        my_sum.next = ListNode()
        my_sum = my_sum.next
        my_sum.val, carry.val = sum_and_carry(lst.val + carry.val)
        lst = lst.next
    return my_sum


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = my_sum = ListNode()
    carry = ListNode()

    # Loop through the linked lists and add build the sum list
    while l1 and l2:
        my_sum.val, carry.val = sum_and_carry(l1.val + l2.val + carry.val)
        if l1.next and l2.next:
            my_sum.next = ListNode()
            my_sum = my_sum.next
        l1 = l1.next
        l2 = l2.next

    # Add the remaining elements of the list to the sum
    # At most one of the following two lines will have an effect
    my_sum = add_end_of_list(l1, my_sum, carry)
    my_sum = add_end_of_list(l2, my_sum, carry)

    # Add the carry if there is any
    if carry.val:
        my_sum.next = ListNode()
        my_sum.next.val = carry.val

    return head
