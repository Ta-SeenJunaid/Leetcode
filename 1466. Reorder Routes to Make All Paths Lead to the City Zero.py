# https://www.youtube.com/watch?v=m17yOR5_PpI
from typing import List


class Solution:
    def __init__(self):
        self.edges = None
        self.neighbors = None
        self.visited = set()
        self.result = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.edges = {(a, b) for a, b in connections}
        self.neighbors = { city:[] for city in range(n)}
        for a, b in connections:
            self.neighbors[a].append(b)
            self.neighbors[b].append(a)
        self.visited.add(0)
        self.dfs(0)
        return self.result

    def dfs(self, city):
        for neighbor in self.neighbors[city]:
            if neighbor in self.visited:
                continue
            if (neighbor, city) not in self.edges:
                self.result += 1
            self.visited.add(neighbor)
            self.dfs(neighbor)


solution = Solution()
print(solution.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
# print(solution.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
# print(solution.minReorder(n = 3, connections = [[1,0],[2,0]]))