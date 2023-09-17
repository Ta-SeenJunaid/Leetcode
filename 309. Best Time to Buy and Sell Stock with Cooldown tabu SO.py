class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre1 = [0 for _ in range(2)]
        pre2 = [0 for _ in range(2)]
        for idx in range(len(prices)-1, -1, -1):
            cur = [0 for _ in range(2)]
            cur[1] = max(-prices[idx] + pre1[0], pre1[1])
            cur[0] = max(prices[idx] + pre2[1], pre1[0])
            pre2 = pre1
            pre1 = cur
        return pre1[1]
