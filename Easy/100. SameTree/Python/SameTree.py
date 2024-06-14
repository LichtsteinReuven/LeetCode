# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My solution
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    # Base case: if one of the nodes is None, and the other is not, return False
    if (p is None and q is not None) or (p is not None and q is None):
        return False
    # Base case: if both nodes are None, return True
    if p is None and q is None:
        return True
    # Base case: if the values of the nodes are different, return False
    if p.val != q.val:
        return False
    # Recursive case: return the result of comparing the right and left subtrees
    return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
