#二分法
#https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
class Solution:
    def mySqrt(self, x:int):
        if x == 0:
            return 0
        left = 1
        right = x
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return left