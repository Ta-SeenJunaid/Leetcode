# https://leetcode.com/problems/target-sum/solutions/3171862/recursion-to-memoization-in-single-line-solution/
from functools import lru_cache
from typing import List


# class Solution:
#     def __init__(self):
#         self.memo = None
#
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         nums_sum = sum(nums)
#         n = len(nums)
#         if target > nums_sum:
#             return 0
#         t_sum = (nums_sum+target)//2
#         self.memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
#         return self.count_sub_set_sum(nums, t_sum, n)
#
#     def count_sub_set_sum(self, nums, t_sum, n):
#         if t_sum == 0:
#             self.memo[n][t_sum] = 1
#             return self.memo[n][t_sum]
#         if n == 0:
#             self.memo[n][t_sum] = 0
#             return self.memo[n][t_sum]
#         if self.memo[n][t_sum] != -1:
#             return self.memo[n][t_sum]
#         if nums[n-1] > t_sum:
#             self.memo[n][t_sum] = self.count_sub_set_sum(nums, t_sum, n-1)
#             return self.memo[n][t_sum]
#         else:
#             self.memo[n][t_sum] = self.count_sub_set_sum(nums, t_sum-nums[n-1], n-1) \
#                                   + self.count_sub_set_sum(nums, t_sum, n-1)
#             return self.memo[n][t_sum]

# class Solution:
#     def __init__(self):
#         self.memo = None
#
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         nums_sum = sum(nums)
#         n = len(nums)
#         if target > nums_sum:
#             return 0
#         t_sum = (nums_sum+target)//2
#         self.memo = [[-1 for i in range(t_sum+1)] for j in range(n+1)]
#         return self.count_sub_set_sum(nums, t_sum, n)
#
#     def count_sub_set_sum(self, a, t_sum, n):
#         table = [[0 for i in range(t_sum + 1)] for j in range(n + 1)]
#         for i in range(n + 1):
#             table[i][0] = 1
#         for i in range(1, n + 1):
#             for j in range(1, t_sum + 1):
#                 if a[i - 1] > j:
#                     table[i][j] = table[i - 1][j]
#                 else:
#                     table[i][j] = table[i - 1][j - a[i - 1]] + table[i - 1][j]
#         return table[n][t_sum]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def rec(index, cur):
            if index == len(nums):
                if cur == target:
                    return 1
                return 0
            return rec(index+1, cur + nums[index]) + rec(index+1, cur - nums[index])
        return rec(0, 0)




solution = Solution()
print(solution.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
print(solution.findTargetSumWays(nums = [1], target = 1))
print(solution.findTargetSumWays(nums = [0,0,0,0,0,0,0,0,1], target = 1))