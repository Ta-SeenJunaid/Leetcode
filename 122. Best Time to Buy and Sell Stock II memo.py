class Solution:
    def __init__(self):
        self.memo = None

    def maxProfit(self, prices: List[int]) -> int:
        self.memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return self.dp_re(prices, 0, 1)

    def dp_re(self, prices: List[int], idx:int, can_buy: int) -> int:
        if idx == len(prices):
            return 0
        if self.memo[idx][can_buy] != -1:
            return self.memo[idx][can_buy]
        if can_buy:
            self.memo[idx][can_buy] = max(-prices[idx] + self.dp_re(prices, idx+1, 0), self.dp_re(prices, idx+1, 1))
            return self.memo[idx][can_buy]
        else:
            self.memo[idx][can_buy] = max(prices[idx] + self.dp_re(prices, idx+1, 1), self.dp_re(prices, idx+1, 0))
            return self.memo[idx][can_buy]
          
