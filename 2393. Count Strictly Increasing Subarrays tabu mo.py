class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        prev, ans = 1, 1 
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                prev += 1
            else:
                prev = 1
            ans += prev
        return ans
