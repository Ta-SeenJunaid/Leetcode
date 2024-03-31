# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/4949181/98-43-easy-solution-with-explanation

class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:

        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                bad_idx = i

            if num == mink:
                left_idx = i

            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res
