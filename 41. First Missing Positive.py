# https://leetcode.com/problems/first-missing-positive/editorial/?envType=daily-question&envId=2024-03-26

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contain_1 = False
        for i in range(n):
            if nums[i] == 1:
                contain_1 = True
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1
        if not contain_1:
            return 1
        for i in range(n):
            val = abs(nums[i])
            if val == n:
                nums[0] = - abs(nums[0])
            else:
                nums[val] = -abs(nums[val])
        
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n+1
        
