"""
利用哈希表
执行用时 :52 ms, 在所有 python3 提交中击败了100.00%的用户
内存消耗 :21.2 MB, 在所有 python3 提交中击败了60.00%的用户
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.hash = {}
        self.ans = []

    def findDuplicateSubtrees(self, root):
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return '#'
        s = str(root.val) + ' ' + self.dfs(root.left) + ' ' + self.dfs(root.right)
        if s not in self.hash:
            self.hash[s] = True
        elif self.hash[s]:
            self.ans.append(root)
            self.hash[s] = False
        return s