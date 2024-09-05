class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pre = [float(inf) for _ in range(amount+1)]
        for a in range(amount + 1):
            if a % coins[0] == 0:
                pre[a] = a // coins[0]
        
        for idx in range(1, len(coins)):
            cur = pre
            for amount in range(amount + 1):
                cur[amount] = min((1 + cur[amount - coins[idx]]) if coins[idx] <= amount else float('inf'), pre[amount])
            pre = cur
        result = pre[-1]
        if result == float('inf'):
            return -1
        return result
