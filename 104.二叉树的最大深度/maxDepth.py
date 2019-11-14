#求二叉树的最大深度-----直接用递归法即可
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root:TreeNode):
        return self.maxDepth(root, 0)
    def max_depth(self, root, depth):
        if not root:
            return depth
        return max(self.max_depth(root.left, depth + 1), self.max_depth(root.right, depth + 1))