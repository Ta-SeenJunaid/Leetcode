from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_p, nums_len = 0, len(nums)
        for fast_p in range(nums_len):
            if nums[fast_p] != 0:
                nums[slow_p], nums[fast_p] = nums[fast_p], nums[slow_p]
                slow_p += 1
        # print(nums)


solution = Solution()
solution.moveZeroes([0,0,1])
solution.moveZeroes([0,1,0,3,12])
solution.moveZeroes([0])