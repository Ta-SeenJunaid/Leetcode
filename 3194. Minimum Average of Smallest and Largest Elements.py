class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        temp = []
        l, r = 0, len(nums) - 1
        while l <= r:
            temp.append((nums[l]+nums[r])/2)
            l += 1
            r -= 1
        return min(temp)
        
