class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pre = [0 for _ in range(2)]
        for idx in range(len(prices)-1, -1, -1):
            cur = [0 for _ in range(2)]
            cur[1] = max(-prices[idx] + pre[0], pre[1])
            cur[0] = max(prices[idx] - fee + pre[1], pre[0])
            pre = cur
        return pre[1]
        
