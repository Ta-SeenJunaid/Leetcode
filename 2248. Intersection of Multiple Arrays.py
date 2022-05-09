from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common_element = set(nums[0])
        for num in nums[1:]:
            common_element &= set(num)
        return list(sorted(common_element))


solution = Solution()
print(solution.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(solution.intersection(nums = [[1,2,3],[4,5,6]]))
print(solution.intersection(nums = [[1,2,3]]))