class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        low, high = 1, len(nums) - 2
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
