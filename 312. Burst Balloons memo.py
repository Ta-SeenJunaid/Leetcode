class Solution:
    def __init__(self):
        self.memo = None

    def maxCoins(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        self.memo = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        return self.bb(1, nums_len, nums)

    def bb(self, i, j, nums):
        if i > j:
            return 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        maxi = 0
        for idx in range(i, j+1):
            maxi = max(maxi, (nums[i-1] * nums[idx] * nums [j+1] + self.bb(i, idx-1, nums) + self.bb(idx+1, j, nums)))
        self.memo[i][j] = maxi
        return maxi
