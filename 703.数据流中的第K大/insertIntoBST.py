"""
超时了，不过这个方法是可以运行的。
这个方法是利用二叉搜索树实现寻找第K大的数字

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.cnt = 1
        self.left = None
        self.right = None


class KthLargest:
    def __init__(self, k, nums):
        if nums:
            self.cur_node = TreeNode(nums[0])
            if len(nums) > 1:
                for i in nums[1:]:
                    self.insertIntoBST(self.cur_node, i)
        else:
            self.cur_node = None
        self.k = k

    def add(self, val: int) -> int:
        if self.cur_node:
            self.cur_node = self.insertIntoBST(self.cur_node, val)
        else:
            self.cur_node = TreeNode(val)
        a = self.search(self.cur_node, self.k)
        print(a)

    def insertIntoBST(self, root, val):

        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        elif root.val >= val:
            root.left = self.insertIntoBST(root.left, val)
        root.cnt += 1
        return root

    def search(self, root, k):
        if k == 0:
            return root.val
        if root.right:
            if k == root.right.cnt + 1:
                return root.val
            elif k > root.right.cnt:
                return self.search(root.left, k - root.right.cnt - 1)
            else:
                return self.search(root.right, k)
        elif root.left:
            if k == 1:
                return root.val
        else:
            return root.val


if __name__ == '__main__':
    a = []
    kthLargest = KthLargest(1, a)
    kthLargest.add(-3)
    kthLargest.add(-2)
    kthLargest.add(-4)
    kthLargest.add(0)
    kthLargest.add(4)

