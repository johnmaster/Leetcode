#树的先序遍历迭代法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preOrderTraversal(self, root: TreeNode):
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.val)
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
        return ans