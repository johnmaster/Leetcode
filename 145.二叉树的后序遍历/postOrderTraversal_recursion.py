#后序遍历二叉树递归法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        ans = []
        self.postorder(root, ans)
        return ans
    def postorder(self, root, ans):
        if not root:
            return
        self.postorder(root.left, ans)
        self.postorder(root.right, ans)
        ans.append(root.val)