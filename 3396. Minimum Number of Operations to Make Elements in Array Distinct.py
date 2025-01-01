from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        f = Counter(nums)
        if len(nums) == len(f):
                    return ans
            
        while True:
            ans +=1
            for i in range(3):
                f[nums[0]] -= 1
                if f[nums[0]] == 0:
                    del f[nums[0]]
                nums.pop(0)
                if len(nums) == len(f):
                    return ans
                if not nums:
                    return ans
        return ans
