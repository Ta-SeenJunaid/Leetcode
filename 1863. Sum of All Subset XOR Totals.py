# 78. Subsets.py need to optimize with bit manipulation later
from typing import List
from operator import ixor
from functools import reduce


class Solution:
    def __init__(self):
        self.result = 0

    def subsetXORSum(self, nums: List[int]) -> List[List[int]]:
        self.dfs_backtrack(0, [], nums)
        return self.result

    def dfs_backtrack(self, idx, sub_set: List, nums: List):
        if idx == len(nums):
            if sub_set:
                self.result += reduce(ixor, sub_set.copy())
            return
        sub_set.append(nums[idx])
        self.dfs_backtrack(idx+1,  sub_set, nums)
        sub_set.pop()
        self.dfs_backtrack(idx+1, sub_set, nums)


solution = Solution()
# print(solution.subsets(nums = [5, 1, 6]))
# print(solution.subsets(nums = [0]))
# print(solution.subsets(nums = [1,3]))
print(solution.subsets(nums = [3,4,5,6,7,8]))
