from typing import List


class Solution:
    def __init__(self):
        self.memo = None

    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums%2 != 0:
            return False
        self.memo = [[-1 for i in range(sum_nums//2 + 1)] for j in range(len(nums)+1)]
        return self.is_sub_set_sum(nums, sum_nums//2, len(nums))

    def is_sub_set_sum(self, nums, t_sum, n):
        if t_sum==0:
            return True
        if n==0:
            return False
        if self.memo[n][t_sum] != -1:
            return self.memo[n][t_sum]
        if nums[n-1] > t_sum:
            self.memo[n][t_sum] = self.is_sub_set_sum(nums, t_sum, n-1)
            return self.memo[n][t_sum]
        else:
            self.memo[n][t_sum] = self.is_sub_set_sum(nums, t_sum-nums[n-1], n-1) \
                or self.is_sub_set_sum(nums, t_sum, n-1)
            return self.memo[n][t_sum]


solution = Solution()
print(solution.canPartition(nums = [1,5,11,5]))
# print(solution.canPartition(nums = [1,2,3,5]))