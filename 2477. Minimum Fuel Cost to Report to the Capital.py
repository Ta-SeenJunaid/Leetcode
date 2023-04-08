# https://www.youtube.com/watch?v=O7Z0kiWVk5c
# https://www.youtube.com/watch?v=I3lnDUIzIG4
from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.result = 0
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        for u, v in roads:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        self.dfs(0, None, seats)
        return self.result

    def dfs(self, node, parent, seats):
        people = 1
        for i in self.adj_list[node]:
            if i != parent:
                people += self.dfs(i, node, seats)
        if node != 0:
            self.result += ceil(people/seats)
        return people


solution = Solution()
print(solution.minimumFuelCost(roads = [[0,1],[0,2],[0,3]], seats = 5))

solution = Solution()
print(solution.minimumFuelCost(roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2))

solution = Solution()
print(solution.minimumFuelCost(roads = [], seats = 1))

