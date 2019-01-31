# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pushLeft(self, root, stack):
        while root is not None:
            stack.append(root)
            root = root.left

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        self.pushLeft(root, stack)
        while len(stack) > 0:
            now = stack[-1]
            stack.pop(len(stack) - 1)
            ret.append(now.val)
            self.pushLeft(now.right, stack)
        return ret
