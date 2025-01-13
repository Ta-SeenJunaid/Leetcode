class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        tabu = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                tabu[i] = 1 + tabu[i-1]
        return sum(tabu)
