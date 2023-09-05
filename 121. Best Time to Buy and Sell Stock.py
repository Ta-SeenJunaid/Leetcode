class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, prices[0]
        for buying_price in prices[1:]:
            cur_profit = buying_price - min_price
            profit = max(profit, cur_profit)
            min_price = min(min_price, buying_price)
        return  profit


solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
