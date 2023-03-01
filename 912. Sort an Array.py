from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


solution = Solution()
print(solution.sortArray(nums = [5,2,3,1]))
print(solution.sortArray(nums = [5,1,1,2,0,0]))