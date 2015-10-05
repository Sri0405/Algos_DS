__author__ = 'sridhar'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if (root == null):
            return node
        if (node.val < root.val):
            root.left = insertNode(root.left, node)
        elif (node.val > root.val):
            root.right = insertNode(root.right, node)
        else:
            root.val = node.val;
        return root

