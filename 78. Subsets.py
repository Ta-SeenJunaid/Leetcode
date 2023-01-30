# https://www.youtube.com/watch?v=REOH22Xwdkk
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs_backtrack(0, [], result, nums)
        return result

    def dfs_backtrack(self, idx, sub_set: List, result: List, nums: List):
        if idx == len(nums):
            result.append(sub_set.copy())
            return
        sub_set.append(nums[idx])
        self.dfs_backtrack(idx+1,  sub_set, result, nums)
        sub_set.pop()
        self.dfs_backtrack(idx+1, sub_set, result, nums)


solution = Solution()
print(solution.subsets(nums = [1,2,3]))
print(solution.subsets(nums = [0]))
