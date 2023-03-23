# https://www.youtube.com/watch?v=AKHGqSvGrJo
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.adj = defaultdict(list)
        self.visited = set()
        self.disconnected = 0

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        for src, dst in connections:
            self.adj[src].append(dst)
            self.adj[dst].append(src)
        for i in range(n):
            if i not in self.visited:
                self.disconnected += 1
                self.dfs(i)
        return self.disconnected-1

    def dfs(self, i):
        if i in self.visited:
            return
        self.visited.add(i)
        for nei in self.adj[i]:
            self.dfs(nei)


solution = Solution()
# print(solution.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))
print(solution.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
# print(solution.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]))