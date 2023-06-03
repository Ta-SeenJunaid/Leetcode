import heapq
from collections import defaultdict
from typing import List

# We need to modify the dijkstra's to handle the maximization since by nature it deals with minimization.
#
# So in order to do that we take the probabilities in negatives.

# Max heap implementation:
# The easiest and ideal solution
# Multiply the values by -1
# There you go. All the highest numbers are now the lowest and vice versa.
# Just remember that when you pop an element to multiply it with -1 in order to get the original value again.

# we are doing this by taking the initial weight of heap as -1


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            adj_list[u].append((v, succProb[i]))
            adj_list[v].append((u, succProb[i]))
        min_heap = [(-1, start)]
        visited = set()
        while min_heap:
            w, n = heapq.heappop(min_heap)
            if n == end:
                return -w
            if n in visited:
                continue
            visited.add(n)
            for nei_n, nei_w in adj_list[n]:
                heapq.heappush(min_heap, (w * nei_w, nei_n))
        return 0



solution = Solution()
print(solution.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))

solution = Solution()
print(solution.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))

solution = Solution()
print(solution.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))