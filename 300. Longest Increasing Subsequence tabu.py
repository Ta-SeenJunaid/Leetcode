class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tabu = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]
        for idx in range(len(nums)-1, -1, -1):
            for pre_idx in range(idx-1, -2, -1):
                tabu[idx][pre_idx+1] = max((1 + tabu[idx + 1][idx + 1]) if (pre_idx == -1 or nums[idx] > nums[pre_idx]) else 0,\
                 tabu[idx+1][pre_idx+1])
        return tabu[0][-1+1]
        
