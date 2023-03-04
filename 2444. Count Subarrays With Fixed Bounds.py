# https://www.youtube.com/watch?v=vwzal4jbEfw
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_found = False
        max_found = False
        start = 0
        min_start = 0
        max_start = 0
        count = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                min_found = False
                max_found = False
                start = i + 1
            if num == minK:
                min_start = i
                min_found = True
            if num == maxK:
                max_start = i
                max_found = True
            if min_found and max_found:
                count += min(min_start, max_start) - start + 1
        return count


solution = Solution()
print(solution.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
print(solution.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))