class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans, lp, rp = 0, 0, len(nums)-1
        while lp <= rp:
            if lp == rp:
                ans += nums[lp]
                break
            ans += int(str(nums[lp]) + str(nums[rp]))
            lp += 1
            rp -= 1
        return ans

