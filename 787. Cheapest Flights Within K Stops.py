import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))
        min_heap = [(0, 0, src)]
        visited = set()
        while min_heap:
            w, s, n = heapq.heappop(min_heap)
            if n in visited:
                continue
            if n == dst:
                return w
            if (n, s) in visited or s > k:
                continue
            visited.add((n, s))
            for nei_n, nei_w in adj_list[n]:
                heapq.heappush(min_heap, (nei_w+w, s+1, nei_n))
        return -1

solution = Solution()
print(solution.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
                                 src = 0, dst = 3, k = 1))

solution = Solution()
print(solution.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))

solution = Solution()
print(solution.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))

solution = Solution()
print(solution.findCheapestPrice(n = 3, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1))

solution = Solution()
print(solution.findCheapestPrice(n = 3, flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], src = 0, dst = 2, k = 2))