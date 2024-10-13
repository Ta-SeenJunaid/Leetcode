class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        nums_len = len(nums)
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, nums_len - 1
            while l < r:
                sum = (num + nums[l] + nums[r])
                if abs(res-target) > abs(sum-target):
                    res = sum
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    return sum
        return res
