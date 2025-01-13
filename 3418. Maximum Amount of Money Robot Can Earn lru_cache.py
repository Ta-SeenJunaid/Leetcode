from functools import lru_cache
from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        rlc = len(coins)
        clc = len(coins[0])

        @lru_cache(None)  
        def dp(r, c, neutralize):
            nonlocal rlc, clc
            if r >= rlc or c >= clc:
                return float('-inf')
            if r == rlc - 1 and c == clc - 1:
                if coins[r][c] >= 0 or neutralize > 0:
                    return max(0, coins[r][c])
                else:
                    return coins[r][c]
            cur_val = coins[r][c]
            max_coins = float('-inf')
            if cur_val < 0:
                if neutralize > 0:
                    max_coins = max(max_coins, dp(r + 1, c, neutralize - 1), dp(r, c + 1, neutralize - 1))
                max_coins = max(max_coins, dp(r + 1, c, neutralize) + cur_val,  dp(r, c + 1, neutralize) + cur_val)
            else:
                max_coins = max(max_coins, dp(r + 1, c, neutralize) + cur_val, dp(r, c + 1, neutralize) + cur_val)
            return max_coins
        return dp(0, 0, 2)
