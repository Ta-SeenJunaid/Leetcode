# https://www.youtube.com/watch?v=_K7oyQlAjv4

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        lp = rp = k
        res = cur_min = nums[k]
        while lp > 0 or rp < len(nums) - 1:
            left = nums[lp-1] if lp > 0 else 0
            right = nums[rp+1] if rp < len(nums) - 1 else 0
            if left > right:
                cur_min = min(cur_min, left)
                lp -= 1
            else:
                cur_min = min(cur_min, right)
                rp += 1
            res = max(res, cur_min * (rp - lp +1))
        return res
