# https://www.youtube.com/watch?v=vc_kz2M-jw4
from typing import List


class Solution:
    def __init__(self):
        self.visited = None
        self.extra = None
        self.distance_node = None
        self.ans = -1

    def longestCycle(self, edges: List[int]) -> int:
        self.visited = [False] * len(edges)
        self.extra = [False] *len(edges)
        self.distance_node = [0] * len(edges)
        for i in range(len(edges)):
            if not self.visited[i]:
                self.dfs(i, 0, edges)
        return self.ans

    def dfs(self, node:int, distance:int, edges: List[int]):
        if node == -1:
            return
        elif not self.visited[node]:
            self.visited[node] = True
            self.extra[node] = True
            self.distance_node[node] = distance
            self.dfs(edges[node], distance+1, edges)
        elif self.extra[node]:
            self.ans = max(self.ans, distance - self.distance_node[node])
        self.extra[node] = False


solution = Solution()
print(solution.longestCycle(edges = [3,3,4,2,3]))

solution = Solution()
print(solution.longestCycle(edges = [2,-1,3,1]))