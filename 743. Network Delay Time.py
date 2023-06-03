# https://www.youtube.com/watch?v=8wysIxzqgPI
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        min_time = 0
        min_heap = [(0, k)]
        visited = set()
        while min_heap:
            w, nd = heappop(min_heap)
            if nd in visited:
                continue
            visited.add(nd)
            min_time = max(min_time, w)
            for nei_n, nei_w in adj_list[nd]:
                if nei_n not in visited:
                    heappush(min_heap, (w + nei_w, nei_n))
        return min_time if len(visited) == n else -1


solution = Solution()
print(solution.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))

solution = Solution()
print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))

solution = Solution()
print(solution.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))

solution = Solution()
print(solution.networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2))