"""
广度优先搜索
碰到最短路径的问题，首先往广度优先搜索想。

执行用时 :684 ms, 在所有 python3 提交中击败了85.42%的用户
内存消耗 :16.4 MB, 在所有 python3 提交中击败了16.44%的用户
参考  https://leetcode-cn.com/problems/01-matrix/solution/pao-ding-jie-niu-yi-bu-yi-bu-xiang-jie-01ju-zhen-1/
思想：
1.首先找到给定节点，判断它是否为0，这个初始节点当作第0层，此时distance为0
2.找到初始节点周围四个坐标，这四个节点当作第一层，此时distance为1，判断它们是否为0
3.再找到这四个节点周围的8个节点，这8个节点当作第二层
4.重复以往，层层递进

利用队列实现广度优先搜索
1.我们设置一个队列，先把初始节点添加进去
2.规定每轮把队列中的所有点取出，这一轮代表着相同的distance，所以distance先加1
3.分别对取出的每个点的坐标判断是否是0，是则返回，否则把这个坐标的邻居放到队列中
4.当这个队列不为空的时候，继续执行步骤2
5.由于题目保证有解，所以之前的每轮使用while True就行，一般情况下使用while queue,即队列不为空的时候
"""


class Solution:
    def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        answer = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                answer[i][j] = self.count(matrix, i, j)
        return answer

    def count(self, matrix, row, col):
        if matrix[row][col] == 0:
            return 0
        else:
            queue, distance = (row, col), 0
            while queue:
                distance += 1
                for _ in range(len(queue)):
                    position = queue.pop(0)
                    for pos_i, pos_j in zip((position[0], position[0], position[0] - 1, position[0] + 1),
                                            (position[1] + 1, position[1] - 1, position[1], position[1])):
                        if matrix[pos_i][pos_j] != 0:
                            queue.append((pos_i, pos_j))
                        else:
                            return distance
