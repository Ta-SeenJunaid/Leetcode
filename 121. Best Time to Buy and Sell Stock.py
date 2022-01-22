class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if len(prices) <= 1:
            return res
        minimum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > minimum:
                res = max(res, prices[i]-minimum)
            else:
                minimum = prices[i]

        return res


solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
