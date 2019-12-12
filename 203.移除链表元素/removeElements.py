"""
执行用时 :64 ms, 在所有 python3 提交中击败了99.04%的用户
内存消耗 :15.6 MB, 在所有 python3 提交中击败了98.79%的用户
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        block = ListNode(None)
        block.next = head
        link1 = block
        link2 = head
        while link2:
            if link2.val == val:
                link1.next = link2.next
                link2 = link2.next
            else:
                link1 = link1.next
                link2 = link2.next
        block = block.next
        return block
                