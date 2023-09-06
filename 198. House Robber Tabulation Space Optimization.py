class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = nums[0]
        for idx in range(1, len(nums)):
            prev1, prev2 = max((nums[idx] + prev2), prev1), prev1
        return prev1
        
