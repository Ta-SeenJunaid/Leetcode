from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd =[]
        for num in nums:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd


solution = Solution()
print(solution.sortArrayByParity(nums = [3,1,2,4]))
print(solution.sortArrayByParity(nums = [0]))

