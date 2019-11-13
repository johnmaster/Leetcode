#中序遍历二叉树迭代法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root:TreeNode):
        stack, ans = [], []
        pre = root
        while pre or stack:
            while pre:
                stack.append(pre)
                pre = pre.left
            pre = stack.pop()
            ans.append(pre.val)
            pre = pre.right
        return ans
