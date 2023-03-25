# https://www.youtube.com/watch?v=KNHvK2enKrc
# https://www.youtube.com/watch?v=FHbbgiccilo
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.visited = set()

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        for i in range(n):
            if i not in self.visited:
                temp = self.dfs(i)
                result += temp * (n - temp)
        return result // 2

    def dfs(self, i):
        if i in self.visited:
            return 0
        stack = [i]
        self.visited.add(i)
        count = 0
        while len(stack) != 0:
            current = stack.pop()
            count += 1
            for node in self.adj_list[current]:
                if node not in self.visited:
                    stack.append(node)
                    self.visited.add(node)
        return count


solution = Solution()
print(solution.countPairs( n = 3, edges = [[0,1],[0,2],[1,2]]))

solution = Solution()
print(solution.countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]))