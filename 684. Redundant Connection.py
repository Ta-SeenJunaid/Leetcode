# https://www.youtube.com/watch?v=FXWRE67PLL0
from typing import List


class Solution:
    def __init__(self):
        self.parent = None
        self.rank = None
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [_ for _ in range(len(edges)+1)]
        self.rank = [1] * (len(edges) + 1)
        for n1, n2 in edges:
            if not self.union(n1, n2):
                return [n1, n2]
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


solution = Solution()
print(solution.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))

solution = Solution()
print(solution.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))