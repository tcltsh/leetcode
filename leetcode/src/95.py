# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root_node, now_node, ans, now_index, total_index):
        if now_index == total_index:
            ans.append(root_node)
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        level = 0
        max_node = 0
        while level < n:
            max_node += pow(2, level)
            level += 1

        ans = []
        self.dfs(TreeNode(1), ans, 1, n)
        return ans



if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(3))
