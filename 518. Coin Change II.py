from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins_len = len(coins)
        dp = [[0 for i in range(amount + 1)] for j in range(coins_len + 1)]
        for i in range(coins_len + 1):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if i == 0:
                    dp[i][j] = 0
                    continue
                if coins[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]


solution = Solution()
print(solution.change(amount = 5, coins = [1,2,5]))
print(solution.change(amount = 3, coins = [2]))
print(solution.change(amount = 10, coins = [10]))