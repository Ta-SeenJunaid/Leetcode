# https://www.youtube.com/watch?v=FPCZsG_AkUgnu
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer, right_pointer = 0 , len(nums)-1
        res = []
        while left_pointer <= right_pointer:
            if nums[left_pointer]*nums[left_pointer] \
                    > nums[right_pointer]*nums[right_pointer]:
                res.append(nums[left_pointer]*nums[left_pointer])
                left_pointer += 1
            else:
                res.append(nums[right_pointer]*nums[right_pointer])
                right_pointer -= 1
        return res[::-1]



solution = Solution()
print(solution.sortedSquares(nums=[-4,-1,0,3,10]))
print(solution.sortedSquares(nums=[-7,-3,2,3,11]))
