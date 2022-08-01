from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dict_ = {}
        for i, num in enumerate(sorted_nums):
            if num not in dict_:
                dict_[num] = i

        for i, num in enumerate(nums):
            nums[i] = dict_[num]

        return nums


solution = Solution()
print(solution.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
print(solution.smallerNumbersThanCurrent(nums = [6,5,4,8]))
print(solution.smallerNumbersThanCurrent(nums = [7,7,7,7]))