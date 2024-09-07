class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            cur = []
            for i in range(len(nums) -1):
                cur.append((nums[i]+nums[i+1])%10)
            nums = cur
        return nums[0]
 
        
