from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_p, odd_p = 0, 1
        temp = [0]*len(nums)
        for num in nums:
            if num%2 == 0:
                temp[even_p] = num
                even_p += 2
            else:
                temp[odd_p] = num
                odd_p += 2
        return temp


solution = Solution()
print(solution.sortArrayByParityII(nums = [4,2,5,7]))
print(solution.sortArrayByParityII(nums = [2,3]))
