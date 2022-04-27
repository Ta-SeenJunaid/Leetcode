from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR of same binary cancel each other or results 0, unique one will remain
        # (n XOR 0) = 0
        result = 0
        for n in nums:
            result = n ^ result

        return result


solution = Solution()
print(solution.singleNumber(nums = [2,2,1]))
print(solution.singleNumber(nums = [4,1,2,1,2]))
print(solution.singleNumber(nums = [1]))
