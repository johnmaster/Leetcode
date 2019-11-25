"""
执行用时 :88 ms, 在所有 python3 提交中击败了82.90%的用户
内存消耗 :15.9 MB, 在所有 python3 提交中击败了5.47%的用户
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val > val:
            if root.left:
                return self.searchBST(root.left, val)
        elif root.val < val:
            if root.right:
                return self.searchBST(root.right, val)
        else:
            return root