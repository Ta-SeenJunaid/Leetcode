from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums_len = len(nums)
        for i in range(nums_len-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


solution = Solution()
print(solution.largestPerimeter(nums = [2,1,2]))
print(solution.largestPerimeter(nums = [1,2,1]))
