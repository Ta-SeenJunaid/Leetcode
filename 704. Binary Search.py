from typing import List


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return self.recursive_binary_search(nums, target, 0, len(nums) - 1)
#
#     def recursive_binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
#
#         if left > right:
#             return -1
#
#         mid = (left + right)//2
#
#         if target < nums[mid]:
#             return self.recursive_binary_search(nums, target, left, mid - 1)
#         if target > nums[mid]:
#             return self.recursive_binary_search(nums, target, mid + 1, right)
#
#         return mid


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            elif target > nums[mid] :
                left = mid + 1
        return -1


solution = Solution()
print(solution.search(nums = [-1,0,3,5,9,12], target = 9))
print(solution.search(nums = [-1,0,3,5,9,12], target = 2))
