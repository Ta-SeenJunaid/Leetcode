from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        ans = [None]*len(nums)
        for num in nums:
            if num >= 0:
                ans[even] = num
                even += 2
            else:
                ans[odd] = num
                odd +=2
        return ans


solution = Solution()
print(solution.rearrangeArray(nums = [3,1,-2,-5,2,-4]))
print(solution.rearrangeArray(nums = [-1,1]))
