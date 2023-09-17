class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = [[0 for _ in range(3)] for _ in range(2)]
        cur = [[0 for _ in range(3)] for _ in range(2)]
        for i in range(len(prices)-1, -1, -1):
            for j in range(2):
                for k in range(3):
                    if k==0:
                        continue
                    if j:
                        cur[j][k] = max(-prices[i] + pre[0][k], pre[1][k])
                    else:
                        cur[j][k] = max(prices[i] + pre[1][k-1], pre[0][k])
            pre = cur
        
        # because at 1st case we can not sell, we only can buy or cannot buy. We want the result for 2 transactions.
        return pre[1][2]
