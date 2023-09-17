class Solution:
    def __init__(self):
        self.memo = None
    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.memo = [[-1.1 for _ in range(2)] for _ in range(len(prices))]
        return self.dp_re(0, 1, prices, fee)

    def dp_re(self, idx:int, can_buy: int, prices: List[int], fee: int) -> int:
        if idx == len(prices):
            return 0
        if self.memo[idx][can_buy] != -1.1:
            return self.memo[idx][can_buy]
        if can_buy:
            self.memo[idx][can_buy] = max(-prices[idx] + self.dp_re(idx+1, 0, prices, fee), \
            self.dp_re(idx+1, 1, prices, fee))
            return self.memo[idx][can_buy]
        else:
            self.memo[idx][can_buy] = max(prices[idx]- fee + self.dp_re(idx+1, 1, prices, fee), \
            self.dp_re(idx+1, 0, prices, fee))
            return self.memo[idx][can_buy]
