class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dp(i, cur_val):
            if i == len(nums):
                if cur_val == target:
                    return 1
                else:
                    return 0
            if (i, cur_val) in memo:
                return memo[(i, cur_val)]
            memo[(i, cur_val)] = dp(i+1, cur_val+nums[i]) + dp(i+1, cur_val-nums[i])
            return memo[(i, cur_val)]
        return dp(0, 0) 
