class Solution:
    def rob(self, nums: List[int]) -> int:
        tab = [0 for _ in range(len(nums))]
        tab[0] = nums[0]
        for idx in range(1, len(nums)):
            tab[idx] = max(nums[idx] + (tab[idx-2] if tab[idx-2] else 0), tab[idx-1])
        return tab[-1]
        
