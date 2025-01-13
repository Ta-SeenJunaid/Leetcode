class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            if i > 0 and nums[i] > nums[i-1]:
                memo[i] = 1 + dp(i-1)
                return memo[i]
            memo[i] = 1
            return 1
        return sum(dp(i) for i in range(len(nums)))
        
