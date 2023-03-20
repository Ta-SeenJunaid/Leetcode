# https://www.youtube.com/watch?v=H9bfqozjoqs
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We can put the default value
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1


solution = Solution()
print(solution.coinChange(coins = [1,2,5], amount = 11))
print(solution.coinChange(coins = [2], amount = 3))
print(solution.coinChange(coins = [1], amount = 0))