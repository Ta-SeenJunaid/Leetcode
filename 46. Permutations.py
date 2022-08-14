from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.result

    def backtrack(self, nums, path):
        if not nums:
            self.result.append(path)
        for i in range(len(nums)):
            # print(nums[:i]+nums[i+1:]," ", path+[nums[i]])
            self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]])


solution = Solution()
print(solution.permute(nums = [1,2,3]))
# print(solution.permute(nums = [0,1]))
# print(solution.permute(nums = [1]))
# print(solution.permute(nums = [1,2,3,4]))