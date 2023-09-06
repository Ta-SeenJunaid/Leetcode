class Solution:
    def __init__(self):
        self.memo = None

    def rob(self, nums: List[int]) -> int:
        self.memo = [-1 for _ in range(len(nums))]
        return self.dp_re(nums, len(nums)-1)

    def dp_re(self, nums: List[int], idx: int):
        if idx == 0:
            return nums[0]
        if idx < 0:
            return 0
        if self.memo[idx] != -1:
            return self.memo[idx]
        self.memo[idx] = max((nums[idx] + self.dp_re(nums, idx - 2), self.dp_re(nums, idx-1)))
        return self.memo[idx]
