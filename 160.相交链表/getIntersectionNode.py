"""
根据题目的意思
如果两个链表相交，那么相交点之后的长度是相同的。
我们需要做的事情是，让两个链表从同距离末尾同等距离的位置开始遍历
这个位置只能是较短链表的头结点位置。
为此，我们必须消除两个链表的长度差
1.指针pA指向A链表，指针pB指向B链表，依次往后遍历。
2.如果pA到了末尾，则pA = headB继续遍历。
3.如果pB到了末尾，则pB = headA继续遍历。
4.比较长的链表指针指向较短链表的head时，长度差就可以消除了。
5.如此，只需要将最短链表遍历两次即可找到位置

执行用时 :168 ms, 在所有 python3 提交中击败了78.97%的用户
内存消耗 :27.7 MB, 在所有 python3 提交中击败了100.00%的用户

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha