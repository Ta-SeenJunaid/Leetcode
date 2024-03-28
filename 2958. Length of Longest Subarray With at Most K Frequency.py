class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        f_c = defaultdict(int)
        l_p = 0
        for r_p in range(len(nums)):
            f_c[nums[r_p]] += 1
            if f_c[nums[r_p]] <= k:
                ans = max(ans, r_p - l_p + 1)
            else:
                while f_c[nums[r_p]] > k and l_p <= r_p:
                    f_c[nums[l_p]] -= 1
                    l_p += 1                
        return ans
        
