# https://www.youtube.com/watch?v=CZ-z1ViskzE

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        ans, l_p, max_num_cnt = 0, 0, 0
        for r_p in range(len(nums)):
            if nums[r_p] == max_num:
                max_num_cnt += 1
            while max_num_cnt > k or (l_p <= r_p and max_num_cnt==k and nums[l_p]!= max_num):
                if nums[l_p] == max_num:
                    max_num_cnt -= 1
                l_p += 1
            if max_num_cnt == k:
                ans += l_p + 1
        return ans
        
