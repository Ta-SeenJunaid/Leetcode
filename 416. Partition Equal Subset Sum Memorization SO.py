class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n_sum = sum(nums)
        if n_sum % 2 != 0:
            return False
        pre = [False for _ in range(n_sum//2 + 1)]
        pre[0] = True
        for i in range(1, len(nums)):
            cur = [False for _ in range(n_sum//2 + 1)]
            cur[0] = True
            for target in range(1, n_sum//2 + 1):
                cur[target] = (nums[i] <= target and pre[target-nums[i]]) or pre[target]
            pre = cur
        return pre[-1]
