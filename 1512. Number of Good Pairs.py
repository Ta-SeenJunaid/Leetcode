from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count


solution = Solution()
print(solution.numIdenticalPairs(nums = [1,2,3,1,1,3]))
print(solution.numIdenticalPairs(nums = [1,1,1,1]))
print(solution.numIdenticalPairs(nums = [1,2,3]))
