#二叉树的层次遍历-递归法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root:TreeNode):
        ans = []
        self.levelTraversal(root, ans, 0)
        return ans
    def levelTraversal(self, root, ans, depth):
        if not root:
            return
        if len(ans) == depth:
            ans.append([])
        ans[depth].append(root.val)
        self.levelTraversal(root.left, ans, depth + 1)
        self.levelTraversal(root.right, ans, depth + 1)
