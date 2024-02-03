# https://leetcode.com/problems/partition-array-for-maximum-sum/solutions/4668715/beats-100-users-easy-understood-solution-with-optimized-space-3-approaches 

class Solution:
    def __init(self):
        self.n = 0
        self.memo = None

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.n = len(arr)
        self.memo = [-1 for _ in range(self.n)]
        return self.dfs_helper(arr, k, 0)

    def dfs_helper(self, arr, k, ind):
        if ind == self.n:
            return 0
        if self.memo[ind] != -1:
            return self.memo[ind]
        cur_max = lar_sum = 0
        for j in range(ind, min(ind+k, self.n)):
            cur_max = max(cur_max, arr[j])
            temp = cur_max*(j-ind+1) + self.dfs_helper(arr, k, j+1)
            lar_sum = max(temp, lar_sum) 
        self.memo[ind] = lar_sum
        return self.memo[ind]
