class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(ix):
            if ix >= len(nums) - 1:
                return 0
            if ix in memo:
                return memo[ix]
            if nums[ix] == 0:
                return float('inf')
            temp = float("inf")
            for i in range(1, nums[ix]+1):
                temp = min(temp, 1 + dp(ix+i))
            memo[ix] = temp
            return memo[ix]
        return dp(0)
