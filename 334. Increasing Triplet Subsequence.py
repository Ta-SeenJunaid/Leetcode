from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first_small = second_small = float('inf')
        for num in nums:
            if num <= first_small:
                first_small = num
            elif num <= second_small:
                second_small = num
            else:
                return True
        return False


solution = Solution()
print(solution.increasingTriplet(nums = [1,2,3,4,5]))
print(solution.increasingTriplet(nums = [5,4,3,2,1] ))
print(solution.increasingTriplet(nums = [2,1,5,0,4,6]))