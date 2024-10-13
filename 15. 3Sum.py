# https://www.youtube.com/watch?v=jzZsG8n2R9A
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        ans = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, nums_len -1
            while l < r:
                sum3 = num + nums[l] + nums[r]
                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    ans.append([num, nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans
        
