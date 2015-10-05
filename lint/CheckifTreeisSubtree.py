__author__ = 'sridhar'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def areidentical(self, T1, T2):

        if T1 == None and T2 == None:
            return True
        if T1 == None or T2 == None:
            return False

        return T1.val == T2.val and self.areidentical(T1.left, T2.left) and self.areidentical(T1.right, T2.right)

    def isSubtree(self, T1, T2):

        if T2 is None:
            return True

        if T1 is None:
            return False

        if self.areidentical(T1,T2):
            return True

        return self.isSubtree(T1.left,T2) or self.isSubtree(T1.right,T2)

# write your code here
