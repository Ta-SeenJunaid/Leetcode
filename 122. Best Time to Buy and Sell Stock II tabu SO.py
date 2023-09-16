class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = [0, 0]
        for row in range(len(prices)-1,-1, -1):
            cur = [0, 0]
            for col in range(2):
                if col:
                    cur[col] = max(-prices[row] + pre[0], pre[1])
                else:
                    cur[col] = max(prices[row] + pre[1], pre[0])
            pre = cur

        # Why not tab[0][0], because at 1st case we can not sell, we only can buy or cannot buy.
        return pre[-1]
      
