# https://www.youtube.com/watch?v=tmSYez2tyW4
import math
from heapq import heappush, heappop, heapify, heapreplace
from typing import List

# class Solution:
#     def minStoneSum(self, piles: List[int], k: int) -> int:
#         heap = []
#         for i in piles:
#             heappush(heap, -1*i)
#         for i in range(k):
#             x = -1*heappop(heap)
#             x = math.ceil(x/2)
#             heappush(heap, -1*x)
#         return -1*sum(heap)


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-n for n in piles]
        heapify(piles)
        for i in range(k):
            heapreplace(piles, piles[0] // 2)
        return -sum(piles)


solution = Solution()
print(solution.minStoneSum(piles = [5,4,9], k = 2))
print(solution.minStoneSum(piles = [4,3,6,7], k = 3))