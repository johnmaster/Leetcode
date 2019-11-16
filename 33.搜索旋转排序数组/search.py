class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        size = len(nums)
        left = 0
        right = size - 1
        #利用二分查找寻找出旋转点，mid值始终与right比较
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        rev = left
        left = 0
        right = size - 1
        #找出旋转点后，利用mid加旋转点位置与长度求余得出真实位置
        while left < right:
            mid = left + (right - left) // 2
            realmid = (mid + rev) % size
            if nums[realmid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[(left + rev) % size] == target:
            return (left + rev) % size
        else:
            return - 1
