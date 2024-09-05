class Solution:
    def __init__(self):
        self.memo = None

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        result = self.dp_helper(coins, len(coins)-1, amount, 0)
        if result == float('inf'):
            return -1
        return result 

    def dp_helper(self, coins, idx, amount, cur_count):
        if idx == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return float('inf')
        if self.memo[idx][amount] != -1:
            return self.memo[idx][amount]
        self.memo[idx][amount] =  min((1 + self.dp_helper(coins, idx, amount - coins[idx], cur_count +1)) if coins[idx] <= amount else float('inf'), self.dp_helper(coins, idx -1, amount, cur_count))
        return self.memo[idx][amount]
