class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root, ans):
        if not root:
            return
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)