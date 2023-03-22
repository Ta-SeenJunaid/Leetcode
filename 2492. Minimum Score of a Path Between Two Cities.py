# https://www.youtube.com/watch?v=K7-mXA0irhY
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.res = float("inf")
        self.visited = set()
        self.adj = defaultdict(list)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        for src, dst, dist in roads:
            self.adj[src].append((dst, dist))
            self.adj[dst].append((src, dist))
        self.dfs(1)
        return self.res


    def dfs(self, i):
        if i in self.visited:
            return
        self.visited.add(i)
        for nei, dist in self.adj[i]:
            self.res = min(self.res, dist)
            self.dfs(nei)


solution = Solution()
print(solution.minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
# print(solution.minScore(n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]))