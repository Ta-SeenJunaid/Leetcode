class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums <= 2:
            return nums.reverse()
        fi_p, se_p = len(nums) - 2, len(nums) - 1
        while fi_p >= 0:
            if nums[fi_p] >= nums[fi_p+1]:
                fi_p -= 1
            else:
                while se_p > fi_p:
                    if nums[se_p] <= nums[fi_p]:
                        se_p -= 1
                    else:
                        nums[fi_p], nums[se_p] =  nums[se_p], nums[fi_p]
                        nums[fi_p+1:len_nums] = reversed(nums[fi_p+1:len_nums])
                        return nums
        return nums.reverse()
        
