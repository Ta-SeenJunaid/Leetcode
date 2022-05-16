from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            nums.append(nums[nums[i]])
        return nums[length:]


solution = Solution()
print(solution.buildArray(nums = [0,2,1,5,3,4]))
print(solution.buildArray(nums = [5,0,1,2,3,4]))