__author__ = 'sridhar'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return sys.maxint
        if root.left is None and root.right is None:
            return 1
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)

            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
