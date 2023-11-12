class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        lp, rp = 0, len(nums)-1
        while nums[rp] > 0 and lp < rp:
            if abs(nums[lp]) == nums[rp] and nums[lp] < 0:
                return nums[rp]
            elif abs(nums[lp]) < nums[rp]:
                rp -= 1
            else:
                lp += 1
        return -1
