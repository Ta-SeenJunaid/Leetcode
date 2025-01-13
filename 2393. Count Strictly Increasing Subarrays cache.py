from functools import lru_cache

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i < 0:
                return 0
            if i > 0 and nums[i] > nums[i-1]:
                return 1 + dp(i-1)
            return 1
        return sum(dp(i) for i in range(len(nums)))
        
