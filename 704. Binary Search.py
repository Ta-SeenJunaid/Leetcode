from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive_binary_search(nums, target, 0, len(nums) - 1)

    def recursive_binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:

        if left > right:
            return -1

        mid = (left + right)//2

        if target < nums[mid]:
            return self.recursive_binary_search(nums, target, left, mid -1)
        if target > nums[mid]:
            return self.recursive_binary_search(nums, target, mid +1, right)

        return mid
