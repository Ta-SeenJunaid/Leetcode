from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.insert(index[i], nums[i])

        return output


solution = Solution()
print(solution.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
print(solution.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
