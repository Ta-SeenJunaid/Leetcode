class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if money - prices[0] - prices[1] >= 0:
            return money - prices[0] - prices[1]
        return money
        
