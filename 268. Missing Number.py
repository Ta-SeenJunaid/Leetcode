from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if num!=i:
                return i
        return len(nums)



solution = Solution()
print(solution.missingNumber(nums=[3,0,1]))
print(solution.missingNumber(nums=[0,1]))
print(solution.missingNumber(nums=[9,6,4,2,3,5,7,0,1]))
print(solution.missingNumber(nums=[1]))

