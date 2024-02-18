class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        tabu =[[0 for _ in range(len(nums)+2)] for _ in range(len(nums)+2)]
        nums_len = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        for i in range(nums_len, 0, -1):
            for j in range(1, nums_len+1, 1):
                if i > j:
                    continue
                maxi = 0
                for idx in range(i, j+1):
                    maxi = max(maxi, (nums[i-1] * nums[idx] * nums [j+1] + tabu[i][idx-1] + tabu[idx+1][j]))
                tabu[i][j] = maxi
        return tabu[1][nums_len]
