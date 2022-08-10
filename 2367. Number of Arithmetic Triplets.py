from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # count = 0
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         if nums[j]-nums[i] == diff:
        #             for k in range(j+1, len(nums)):
        #                 if nums[k] - nums[j] == diff:
        #                     count += 1
        # return count

        # https://www.youtube.com/watch?v=veemPBbVjTQ
        res = 0
        for i in nums:
            if i - diff in nums and i + diff in nums:
                res += 1
        return res



solution = Solution()
print(solution.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
print(solution.arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))

