class Solution:
    def lowerbound(self, nums:List[int], target: int):
        low, high, ans = 0, len(nums)-1, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def upperbound(self, nums:List[int], target: int):
        low, high, ans = 0, len(nums)-1, 0
        while low <= high:
            mid = (low+high)//2
            if nums[mid] <= target:
                ans = mid
                low = mid+1
            else:
                high = mid -1
        return ans


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        temp = self.lowerbound(nums, target)
        return [temp, self.upperbound(nums, target)] if nums[temp]== target  \
                    else  [-1, -1]
