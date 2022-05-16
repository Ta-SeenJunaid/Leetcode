from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sum = 0
        for i in range(0, length):
            sum += nums[i]
            nums.append(sum)
        return nums[length:]


solution = Solution()
print(solution.runningSum(nums = [1,2,3,4]))
print(solution.runningSum(nums = [1,1,1,1,1]))
print(solution.runningSum(nums = [3,1,2,10,1]))
