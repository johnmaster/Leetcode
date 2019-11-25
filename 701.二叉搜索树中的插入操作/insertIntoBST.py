"""
执行用时 :152 ms, 在所有 python3 提交中击败了53.16%的用户
内存消耗 :15.9 MB, 在所有 python3 提交中击败了5.88%的用户
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root
