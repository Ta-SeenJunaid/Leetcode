from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count, nums_len, sum_nums = 0, len(nums), sum(nums)
        while sum_nums > 0:
            current_min = 101
            for i in range(nums_len):
                if nums[i] != 0 and nums[i] < current_min:
                    current_min = nums[i]
            for i in range(nums_len):
                if nums[i] >= current_min:
                    nums[i] -= current_min
            count += 1
            sum_nums = sum(nums)
        return count


solution = Solution()
print(solution.minimumOperations(nums = [1,5,0,3,5]))
print(solution.minimumOperations(nums = [0]))
