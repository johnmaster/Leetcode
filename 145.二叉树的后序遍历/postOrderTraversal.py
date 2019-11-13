#后序遍历二叉树-迭代法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        stack, ans = [root], []
        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.val)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
        return ans[::-1]
