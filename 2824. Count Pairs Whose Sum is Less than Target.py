class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        lp, rp, res = 0, len(nums) - 1, 0
        while lp < rp:
            print(lp, rp, nums[rp] - nums[lp])
            if nums[rp] - nums[lp] < target:
                res += rp - lp
                lp += 1
            else:
                rp -= 1
        return res
