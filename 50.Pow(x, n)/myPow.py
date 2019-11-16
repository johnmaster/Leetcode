#计算X的n次幂函数
class Solution(object):
    def myPow(self, x, n):
        numbers = abs(n)
        ans = 1
        while numbers:
            if numbers % 2 != 0:
                ans = ans * x
            x = x * x
            numbers = numbers // 2
        if n < 0:
            return 1 / ans
        else:
            return ans