"""
执行用时 :76 ms, 在所有 python3 提交中击败了24.69%的用户
内存消耗 :16.1 MB, 在所有 python3 提交中击败了43.94%的用户
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        return self.dfs(root)

    def dfs(self, node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not self.dfs(node.right, val, upper):
            return False
        if not self.dfs(node.left, lower, val):
            return False
        return True
