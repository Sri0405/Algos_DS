class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        curr = root
        stack = []
        used = set()
        soln = []

        if curr is not None:
            stack.append(curr)

        while len(stack) > 0:
            curr = stack.pop()
            if curr in used:
                soln.append(curr.val)
            else:
                used.add(curr)
                stack.append(curr)
                if curr.right is not None:
                    stack.append(curr.right)
                if curr.left is not None:
                    stack.append(curr.left)
        return soln

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        solution = []
        used = set()
        stack = []
        if root != None:
            stack.append(root)
        while len(stack)>0:
            node = stack.pop()
            if node in used:
                solution.append(node.val)
            else:
                used.add(node)
                stack.append(node)
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
        return solution
