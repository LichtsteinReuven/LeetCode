
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


visited = {}


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return head
    root = Node(head.val)
    visited[head] = root
    if head.next not in visited:
        root.next = copyRandomList(head.next)
    else:
        root.next = visited[head.next]
    if head.random not in visited:
        root.random = copyRandomList(head.random)
    else:
        root.random = visited[head.random]
    return root