class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.preorder = None
        self.inorder = None
    def buildTree(self, preorder, inorder):
        if len(preorder) != len(inorder):
            return False
        size = len(preorder)
        self.preorder = preorder
        self.inorder = inorder
        return self._dfs(0, size - 1, 0, size - 1)
    def _dfs(self, pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right or in_left > in_right:
            return
        root = TreeNode(self.preorder[pre_left])
        position = self.inorder.index(self.preorder[pre_left])
        root.left = self._dfs(pre_left + 1, position - in_left + pre_left, in_left, position - 1)
        root.right = self._dfs(position - in_left + pre_left + 1, pre_right, position + 1, in_right)
        return root