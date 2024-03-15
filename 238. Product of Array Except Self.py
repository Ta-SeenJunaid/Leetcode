# https://leetcode.com/problems/product-of-array-except-self/solutions/4877147/creative-approach-focus-on-the-number-of-zeros-time-o-n-space-o-1

# Cornar case: two 0 present

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            product *= num
        if zeros == 0:
            for i in range(len(nums)):
                output[i] = product//nums[i]
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = product
        return output

            
        
