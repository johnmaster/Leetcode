class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            temp = guess(mid)
            if temp == 1:
                left = mid + 1
            else:
                right = mid
        return left