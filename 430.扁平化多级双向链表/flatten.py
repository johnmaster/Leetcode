"""
深度优先搜索
执行用时 :40 ms, 在所有 python3 提交中击败了99.40%的用户
内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        if not head:
            return head
        stack, pre = [head], None
        while stack:
            flag = stack.pop()
            if flag.next:
                stack.append(flag.next)
            if flag.child:
                stack.append(flag.child)
                flag.child = None
            if pre:
                pre.next = flag
                flag.prev = pre
            pre = flag
        return head