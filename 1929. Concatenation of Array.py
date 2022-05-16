from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


solution = Solution()
print(solution.getConcatenation(nums = [1,2,1]))
print(solution.getConcatenation(nums = [1,3,2,1]))
