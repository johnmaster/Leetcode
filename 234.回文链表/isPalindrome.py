"""
执行用时 :112 ms, 在所有 python3 提交中击败了18.04%的用户
内存消耗 :30.5 MB, 在所有 python3 提交中击败了5.09%的用户

首先把链表存储在另一个链表中，然后翻转原链表，最后依次比较即可。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        previous, pre = ListNode(None), head
        pre_1 = previous
        while pre:
            pre_1.next = ListNode(pre.val)
            pre_1 = pre_1.next
            pre = pre.next
        previous = previous.next

        pre_2, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre_2
            pre_2 = cur
            cur = temp

        while previous:
            if pre_2.val != previous.val:
                return False
            else:
                pre_2 = pre_2.next
                previous = previous.next
        return True
    