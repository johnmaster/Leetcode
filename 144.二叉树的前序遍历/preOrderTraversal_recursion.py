class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root:TreeNode):
        ans = []
        self.preorder(root, ans)
        return ans

    def preorder(self, root, ans):
        if not root:
            return
        ans.append(root.val)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)