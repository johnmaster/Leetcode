"""
回溯法深度优先搜索
执行用时 :40 ms, 在所有 python3 提交中击败了98.37%的用户
内存消耗 :14.5 MB, 在所有 python3 提交中击败了100.00%的用户
回溯算法的第一想法是将链表想象成一张表。链表中每个节点都有两个
指针。因为随即指针给图结构添加了随机性，所以我们可能会访问相同
的节点多次，这样就形成了环。
拷贝的意思是每当遇到一个新的未访问过的节点，都需要创造一个新的
节点。遍历按照深度优先进行，我们需要在回溯的过程中记录已经访问
过的节点，否则因为随机指针的存在我们可能会产生死循环。
算法
1.从头指针开始遍历整个图
我们将链表看成一个图。Head是图的出发节点。
2.当我们遍历到某个点时，如果我们已经有了当前节点的一个拷贝，我
们不需要重复进行拷贝。
3.如果我们还没拷贝过当前节点，我们创造一个新节点，并把该节点放到
已访问字典中。
4.我们针对两种情况进行回溯调用，一个顺着random指针调用，另一个沿
着next指针调用。
"""


class Node:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head):
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)

        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node