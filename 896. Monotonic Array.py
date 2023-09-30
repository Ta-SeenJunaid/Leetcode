class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc_f, dec_f = True, True
        for idx in range(len(nums) - 1):
            if not nums[idx] >= nums[idx+1]:
                dec_f = False
            if not nums[idx] <= nums[idx+1]:
                inc_f = False
        return inc_f or dec_f

