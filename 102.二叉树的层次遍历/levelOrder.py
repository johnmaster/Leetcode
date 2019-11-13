#层次遍历-迭代法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#广度优先搜索
class Solution:
    def levelOrder(self, root:TreeNode):
        if not root:
            return
        ans = []
        queue = [root]
        while queue:
            temp = []
            temp_1 = []
            for i in queue:
                temp.append(i.val)
                if i.left:
                    temp_1.append(i.left)
                if i.right:
                    temp_1.append(i.right)
            ans.append(temp)
            queue = temp_1
        return ans