class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tab = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(prices)+1)]
        for i in range(len(prices)-1, -1, -1):
            for j in range(2):
                for k in range(3):
                    if k==0:
                        continue
                    if j:
                        tab[i][j][k] = max(-prices[i] + tab[i+1][0][k], tab[i+1][1][k])
                    else:
                        tab[i][j][k] = max(prices[i] + tab[i+1][1][k-1], tab[i+1][0][k])
        
        # because at 1st case we can not sell, we only can buy or cannot buy. We want the result for 2 transactions.
        return tab[0][1][2]
      
