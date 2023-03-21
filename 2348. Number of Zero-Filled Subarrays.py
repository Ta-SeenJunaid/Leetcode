# https://leetcode.com/problems/number-of-zero-filled-subarrays/editorial/
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, num_sub_array = 0, 0
        for num in nums:
            if num == 0:
                num_sub_array += 1
            else:
                num_sub_array = 0
            ans += num_sub_array
        return ans


solution = Solution()
print(solution.zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4]))
print(solution.zeroFilledSubarray(nums = [0,0,0,2,0,0]))
print(solution.zeroFilledSubarray(nums = [2,10,2019]))