class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        min_inc = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                inc = nums[i-1] + 1 -nums[i]
                min_inc += inc
                nums[i] = nums[i-1]+1
        return min_inc
        
