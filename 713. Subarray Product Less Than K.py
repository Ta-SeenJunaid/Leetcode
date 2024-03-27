# https://leetcode.com/problems/subarray-product-less-than-k/editorial/?envType=daily-question&envId=2024-03-27 

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans, cur_pro, l_p = 0, 1, 0
        for r_p in range(len(nums)):
            cur_pro *= nums[r_p]
            while cur_pro >= k:
                cur_pro /= nums[l_p]
                l_p += 1
            ans += r_p - l_p + 1
        return ans

        
