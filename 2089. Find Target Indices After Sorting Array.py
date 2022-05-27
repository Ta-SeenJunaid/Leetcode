from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if num == target:
                result.append(i)
            if num > target:
                break
        return result


solution = Solution()
print(solution.targetIndices(nums = [1,2,5,2,3], target = 2))
print(solution.targetIndices(nums = [1,2,5,2,3], target = 3))
print(solution.targetIndices(nums = [1,2,5,2,3], target = 5))
