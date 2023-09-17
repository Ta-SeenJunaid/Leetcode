class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        tab = [[0 for _ in range(2)] for _ in range(len(prices)+1)]
        for idx in range(len(prices)-1, -1, -1):
            tab[idx][1] = max(-prices[idx] + tab[idx+1][0], tab[idx+1][1])
            tab[idx][0] = max(prices[idx] - fee + tab[idx+1][1], tab[idx+1][0])
        return tab[0][1]
      
