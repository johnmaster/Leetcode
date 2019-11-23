"""
处理好边界条件
执行用时 :220 ms, 在所有 python3 提交中击败了97.40%的用户
内存消耗 :16.5 MB, 在所有 python3 提交中击败了5.55%的用户
参考   https://leetcode-cn.com/problems/diagonal-traverse/solution/498dui-jiao-xian-bian-li-by-zhangll/
"""
class Solution:
    def findDiagonalOrder(self, x):
        if not x:
            return x
        rows = len(x)
        cols = len(x[0])
        pos_i, pos_j, answer = 0, 0, []
        is_up = True
        while True
            answer.append(x[pos_i][pos_j])
            if pos_i == rows - 1 and pos_j == cols - 1:
                return answer
            if is_up:
                if pos_i == rows - 1 and pos_j < cols - 1:
                    pos_j += 1
                    is_up = False
                elif pos_j ==cols - 1:
                    pos_i += 1
                    is_up = False
                else:
                    pos_i -= 1
                    pos_j += 1
            else:
                if pos_j == 0 and pos_i < rows - 1:
                    pos_i += 1
                    is_up = True
                elif pos_i == rows - 1:
                    pos_j += 1
                    is_up = True
                else:
                    pos_i += 1
                    pos_j -= 1
