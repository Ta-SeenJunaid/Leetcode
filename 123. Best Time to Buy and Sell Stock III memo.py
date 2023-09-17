class Solution:
    def __init__(self):
        self.memo = None

    def maxProfit(self, prices: List[int]) -> int:
        self.memo = [[[-1.1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices))]
        return self.dp_re(prices, 0, 1, 2)

    def dp_re(self, prices: List[int], idx:int, can_buy: int, remaining_transactions: int):
        if idx==len(prices):
            return 0
        if remaining_transactions == 0:
            return 0
        if self.memo[idx][can_buy][remaining_transactions] != -1.1:
            return self.memo[idx][can_buy][remaining_transactions]
        if can_buy:
            self.memo[idx][can_buy][remaining_transactions] = max(-prices[idx] + self.dp_re(prices, idx+1, 0, remaining_transactions), \
            self.dp_re(prices, idx+1, 1, remaining_transactions))
            return self.memo[idx][can_buy][remaining_transactions]
        else:
            self.memo[idx][can_buy][remaining_transactions] = max(prices[idx] + self.dp_re(prices, idx+1, 1, remaining_transactions-1), \
            self.dp_re(prices, idx+1, 0, remaining_transactions))
            return self.memo[idx][can_buy][remaining_transactions]
            
