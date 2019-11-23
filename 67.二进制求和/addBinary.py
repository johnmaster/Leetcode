"""
执行用时 :44 ms, 在所有 python3 提交中击败了81.43%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.24%的用户
在短的字符串前面补0
"""


class Solution:
    def addBinary(self, a, b):
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        carry = 0
        pos_a, pos_b = len(a) - 1, len(b) - 1
        answer = ''
        while pos_a >= 0:
            temp = int(a[pos_a]) + int(b[pos_b]) + carry
            if temp >= 2:
                carry = 1
                temp %= 2
            else:
                carry = 0
            answer = str(temp) + answer
            pos_a, pos_b = pos_a - 1, pos_b - 1
        if carry == 1:
            return '1' + answer
        else:
            return answer
