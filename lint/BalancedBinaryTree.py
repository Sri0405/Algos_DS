"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:

    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.right), self.getHeight(root.left))

    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True
        else:
            check= root.getHeight(root.left) - root.getHeight(root.right)
            if check>1 or check<-1:
                return False 
            return self.isBalanced(root.right) and self.isBalanced(root.left)
