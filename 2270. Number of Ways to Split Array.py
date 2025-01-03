class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        l_s = 0
        r_s = sum(nums)
        for i in range(n-1):
            l_s += nums[i]
            r_s -= nums[i]
            if l_s >= r_s:
                ans += 1
        return ans
        
