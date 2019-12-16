"""
拉链法
执行用时 :2632 ms, 在所有 python3 提交中击败了5.24%的用户
内存消耗 :48.4 MB, 在所有 python3 提交中击败了5.80%的用户

讨论以下哈希表的性能
复杂度分析：
如果总共有M个键，那么在使用哈希表的时候，可以很容易地达到 O(M)
的空间复杂度。
哈希表的时间复杂度与设计有很强的关系。
我们中的大多数人可能已经在每个桶中使用数组来将值存储在同一个桶
中，理想情况下，桶的大小足够小时，可以看作是一个常数。插入和
搜索的时间复杂度都是 O(1)。
但在最坏的情况下，桶大小设置为N。则插入时时间复杂度为O(1)。
搜索时为O(N)。

内置哈希表的原理
内置哈希表的典型设计是：
1.键值可以是任何可哈希化的类型。并且属于可哈希类型的值将具有哈希
码。此哈希码将用于映射函数以获取存储区索引。
2.每个桶包含一个数组，用于在初始时将所有值存储在同一个桶中。
3.如果在同一个桶中有太多的值，这些值将被保留在一个高度平衡的二叉
搜索树中。
插入和搜索的平均时间复杂度仍为O(1)。最坏情况下插入和搜索的时间
复杂度是O(logN)。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 100000
        self.hash = [Node(None) for _ in range(self.size)]

    def put(self, key, value):
        p = self.hash[key % self.size]
        node = p.next
        if node:
            node.val = value
        else:
            p.next = Node(value)

    def get(self, key):
        p = self.hash[key % self.size]
        node = p.next
        if node:
            return node.val
        else:
            return -1

    def remove(self, key):
        p = self.hash[key % self.size]
        node = p.next
        if node:
            p.next = node.next