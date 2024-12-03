# https://leetcode.com/problems/maximum-width-ramp/editorial

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indicies = [i for i in range(n)]
        indicies.sort(key= lambda i: (nums[i], i)) 
        max_ramp = 0
        min_index = n
        for i in indicies:
            max_ramp = max(max_ramp, i - min_index)
            min_index = min(min_index, i)
        return max_ramp
