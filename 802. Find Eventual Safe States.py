# https://www.youtube.com/watch?v=Re_v0j0CRsg
from typing import List


class Solution:
    def __init__(self):
        self.safe = {}

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(graph)):
            if self.dfs(i, graph):
                res.append(i)
        return res

    def dfs(self, i, graph: List[List[int]]):
        if i in self.safe:
            return self.safe[i]
        self.safe[i] = False
        for nei in graph[i]:
            if not self.dfs(nei, graph):
                return False
        self.safe[i] = True
        return True


solution = Solution()
print(solution.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))

solution = Solution()
print(solution.eventualSafeNodes(graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]))

