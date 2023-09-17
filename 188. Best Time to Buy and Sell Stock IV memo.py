class Solution:
    def __init__(self):
        self.memo = None

    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.memo = [[[-1.1 for _ in range(k+1)] for _ in range(2)] for _ in range(len(prices))]
        return self.dp_re(0, 1, k, prices)

    def dp_re(self, idx:int, can_buy:int, k:int, prices:List[int]) -> int:
        if idx==len(prices) or k==0:
            return 0
        if self.memo[idx][can_buy][k] != -1.1:
            return self.memo[idx][can_buy][k]
        if can_buy:
            self.memo[idx][can_buy][k] = max(-prices[idx] + self.dp_re(idx+1, 0, k, prices), self.dp_re(idx+1, 1, k, prices))
            return self.memo[idx][can_buy][k]
        else:
            self.memo[idx][can_buy][k] = max(prices[idx] + self.dp_re(idx+1, 1, k-1, prices), self.dp_re(idx+1, 0, k, prices))
            return self.memo[idx][can_buy][k]
            
