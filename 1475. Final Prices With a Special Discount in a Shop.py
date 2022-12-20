from typing import List


# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         result = prices.copy()
#         stack = []
#         for i,v in enumerate(prices):
#             while stack and v<=stack[-1][1]:
#                 index, value = stack.pop()
#                 result[index] = value-v
#             stack.append([i, v])
#         return result

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i,p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                prices[stack.pop()] -= p
            stack.append(i)
        return prices


solution = Solution()
print(solution.finalPrices(prices = [8,4,6,2,3]))
print(solution.finalPrices(prices = [1,2,3,4,5]))
print(solution.finalPrices(prices = [10,1,1,6]))