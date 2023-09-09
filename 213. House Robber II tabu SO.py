class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.dp_tab_helper(nums[1:]), self.dp_tab_helper(nums[:-1]))
    
    def dp_tab_helper(self, nums: List[int]) -> int:
        prev2, prev1 = 0, nums[0]
        for idx in range(1, len(nums)):
            prev1, prev2 = max(nums[idx] + prev2, prev1), prev1
        return prev1
