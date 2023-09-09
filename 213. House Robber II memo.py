class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo1, memo2 = [-1 for _ in range(len(nums)-1)],  [-1 for _ in range(len(nums)-1)]
        return max(self.de_re(nums[1:], len(nums)-2, memo1), self.de_re(nums[:-1], len(nums)-2, memo2))


    def de_re(self, nums: List[int], idx: int, memo):
        if idx == 0:
            return nums[0]
        if idx < 0:
            return 0
        if memo[idx] != -1:
            return memo[idx]
        memo[idx] = max((nums[idx] + self.de_re(nums, idx -2, memo)), self.de_re(nums, idx -1, memo))
        return memo[idx]
