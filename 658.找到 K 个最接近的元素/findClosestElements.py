#双指针法
class Solution(object):
    def findClosestElements(self, arr, k, x):
        size = len(arr)
        left = 0
        right = size - 1
        del_numbers = size - k
        while del_numbers:
            if x - arr[left] > arr[right] - x:
                left += 1
            else:
                right -= 1
            del_numbers -= 1
        return arr[left: right + 1]
