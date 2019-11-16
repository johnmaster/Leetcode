class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid
        if left * left == num:
            return True
        else:
            return False
        