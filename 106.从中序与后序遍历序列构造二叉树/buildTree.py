class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.inorder = None
        self.postorder = None
    def buildTree(self, inorder, postorder):
        assert len(inorder) == len(postorder)
        size = len(inorder)
        self.inorder = inorder
        self.postorder = postorder
        return self._dfs(0, size - 1, 0, size - 1)
    def _dfs(self, in_left, in_right, post_left, post_right):
        if in_left > in_right or post_left > post_right:
            return
        root = TreeNode(self.postorder[post_right])
        position = self.inorder.index(self.postorder[post_right])
        root.left = self._dfs(in_left, position - 1, post_left, post_right - in_right + position - 1)
        root.right = self._dfs(position + 1, in_right, post_right - in_right + position, post_right - 1)
        return root