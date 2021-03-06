from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        # nums.sort(reverse=True)
        # return nums[k-1]


solution = Solution()
print(solution.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(solution.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
