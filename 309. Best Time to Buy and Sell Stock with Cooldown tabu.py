class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tab = [[0 for _ in range(2)] for _ in range(len(prices)+2)]
        for idx in range(len(prices)-1, -1, -1):
            for can_buy in range(2):
                if can_buy:
                    tab[idx][can_buy] = max(-prices[idx] + tab[idx+1][0], tab[idx+1][1])
                else:
                    tab[idx][can_buy] = max(prices[idx] + tab[idx+2][1], tab[idx+1][0])
        return tab[0][1]
