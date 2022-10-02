# need to practice more and more
from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.dp_helper(nums, target)

    def dp_helper(self, nums: List[int], target: int):
        if target == 0:
            return 1
        if target in self.memo:
            return self.memo[target]
        else:
            res = 0
            for num in nums:
                reminder = target - num
                if reminder >= 0:
                    res += self.dp_helper(nums, reminder)
            self.memo[target] = res
            return self.memo[target]


solution = Solution()
print(solution.combinationSum4(nums = [1,2,3], target = 4))
# print(solution.combinationSum4(nums = [9], target = 3))