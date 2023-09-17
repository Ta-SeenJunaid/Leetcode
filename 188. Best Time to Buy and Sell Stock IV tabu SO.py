class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        pre = [[0 for _ in range(k+1)] for _ in range(2)]
        cur = [[0 for _ in range(k+1)] for _ in range(2)]
        for i in range(len(prices)-1, -1, -1):
            for j in range(2):
                for t in range(1, k+1):
                    if j:
                        cur[j][t] = max(-prices[i] + pre[0][t], pre[1][t])
                    else:
                        cur[j][t] = max(prices[i] + pre[1][t-1], pre[0][t])
                pre = cur
        return cur[1][k]
      
