from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            str_num = str(num)
            for digit in str_num:
                digit_sum += int(digit)
        return abs(ans_sum-digit_sum)


solution = Solution()
print(solution.differenceOfSum(nums = [1,15,6,3]))
print(solution.differenceOfSum( nums = [1,2,3,4]))