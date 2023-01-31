from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.visited_path = set()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.dfs_backtrack(nums, [])
        return self.result

    def dfs_backtrack(self, nums, path):
        if not nums:
            self.result.append(path)
            return
        for i in range(len(nums)):
            temp = tuple(path+[nums[i]])
            if temp not in self.visited_path:
                self.visited_path.add(temp)
                self.dfs_backtrack(nums[:i]+nums[i+1:], path+[nums[i]])


solution = Solution()
print(solution.permuteUnique(nums = [1,1,2]))
# print(solution.permuteUnique(nums = [1,2,3]))
