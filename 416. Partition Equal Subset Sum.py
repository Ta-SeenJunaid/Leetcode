# https://www.youtube.com/watch?v=UmMh7xp07kY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=8
# https://www.geeksforgeeks.org/partition-problem-dp-18/
# https://www.youtube.com/watch?v=IsvocB5BJhw
# https://leetcode.com/problems/partition-equal-subset-sum/solutions/633426/python-3-iterative-solution-0-1-knapsack-approach-dp/
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        return self.is_sub_set_sum(nums, nums_sum//2)

    def is_sub_set_sum(self, nums, _sum):
        nums_len = len(nums)
        dp = [[True for i in range(_sum + 1)] for j in range(nums_len + 1)]
        for i in range(nums_len + 1):
            for j in range(_sum + 1):
                if j == 0:
                    dp[i][j] = True
                    continue
                if i == 0:
                    dp[i][j] = False
                    continue
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[nums_len][_sum]


solution = Solution()
print(solution.canPartition(nums=[1, 5, 11, 5]))
print(solution.canPartition(nums=[1, 2, 3, 5]))
print(solution.canPartition(nums=[1,2,3,4,5,6,7]))
print(solution.canPartition(nums=[1,2,5]))

