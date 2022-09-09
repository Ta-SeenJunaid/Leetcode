from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) -1
        ans = 0
        while i < j:
            ans = max(ans, nums[i]+nums[j])
            i += 1
            j -= 1
        return ans


solution = Solution()
print(solution.minPairSum(nums = [3,5,2,3]))
print(solution.minPairSum(nums = [3,5,4,2,4,6]))
