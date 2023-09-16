class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tab = [[0 for _ in range(2)] for _ in range(len(prices)+1)]
        for row in range(len(prices)-1,-1, -1):
            for col in range(2):
                if col:
                    tab[row][col] = max(-prices[row] + tab[row+1][0], tab[row+1][1])
                else:
                    tab[row][col] = max(prices[row] + tab[row+1][1], tab[row+1][0])

        # Why not tab[0][0], because at 1st case we can not sell, we only can buy or cannot buy.
        return tab[0][1]
        
