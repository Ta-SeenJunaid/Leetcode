class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        tab = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(len(prices)+1)]
        for i in range(len(prices)-1, -1, -1):
            for j in range(2):
                for t in range(1, k+1):
                    if j:
                        tab[i][j][t] = max(-prices[i] + tab[i+1][0][t], tab[i+1][1][t])
                    else:
                        tab[i][j][t] = max(prices[i] + tab[i+1][1][t-1], tab[i+1][0][t])
        return tab[0][1][k]
