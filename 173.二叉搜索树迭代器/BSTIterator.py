"""
执行用时 :88 ms, 在所有 python3 提交中击败了89.86%的用户
内存消耗 :20.6 MB, 在所有 python3 提交中击败了5.66%的用户
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        temp = self.stack.pop()
        answer = temp.val
        temp = temp.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return answer

    def hasNext(self):
        return self.stack != []