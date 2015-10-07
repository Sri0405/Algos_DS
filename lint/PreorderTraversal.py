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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        curr = root
        stack =[]
        soltn = []
        
        while curr is not None or len(stack)>0:
            
            if curr is not None:
                soltn.append(curr.val)
                stack.append(curr)
                curr =curr.left
            else:
                curr = stack.pop()
                curr = curr.right
        
        return soltn
                
