# https://www.youtube.com/watch?v=o8XmnEBQrLs
import collections
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.Counter()
        ans, current = 0, 0
        for i in range(len(nums)):
            seen[nums[i]] += 1
            current += nums[i]
            if i - k >= 0:
                seen[nums[i-k]] -= 1
                current -= nums[i-k]
                if seen[nums[i-k]] == 0:
                    del seen[nums[i-k]]
            if i - k + 1 >= 0:
                if len(seen) == k:
                    ans = max(ans, current)
        return ans


solution = Solution()
print(solution.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3))
print(solution.maximumSubarraySum(nums = [4,4,4], k = 3))
print(solution.maximumSubarraySum(nums = [1,1,1,7,8,9], k = 3))
print(solution.maximumSubarraySum(nums = [5,1,3], k = 1))