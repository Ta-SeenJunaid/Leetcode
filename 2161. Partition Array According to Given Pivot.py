from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return less+equal+greater


solution = Solution()
print(solution.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))
print(solution.pivotArray(nums = [-3,4,3,2], pivot = 2))