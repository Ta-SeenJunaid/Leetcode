from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.visited = set()
        self.result = 0
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i !=j and isConnected[i][j] == 1:
                    self.adj_list[i].append(j)
        for i in range(len(isConnected)):
            if i not in self.visited:
                self.result += 1
                self.dfs(i)
        return self.result

    def dfs(self, node):
        self.visited.add(node)
        for i in self.adj_list[node]:
            if i not in self.visited:
                self.dfs(i)




solution = Solution()
print(solution.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))

solution = Solution()
print(solution.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))