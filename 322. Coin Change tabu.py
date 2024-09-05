class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tabu = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        for a in range(amount + 1):
            if a % coins[0] == 0:
                tabu[0][a] = a // coins[0]
            else:
                tabu[0][a] = float(inf)
        
        for idx in range(1, len(coins)):
            for amount in range(amount + 1):
                tabu[idx][amount] =  min((1 + tabu[idx][amount - coins[idx]]) if coins[idx] <= amount else float('inf'), tabu[idx -1][amount])
        result = tabu[-1][-1]
        if result == float('inf'):
            return -1
        return tabu[-1][-1] 

