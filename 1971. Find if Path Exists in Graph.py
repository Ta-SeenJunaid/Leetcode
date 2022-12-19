# https://velog.io/@limelimejiwon/Leetcode-1971.-Find-if-Path-Exists-in-Graph
from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        queue = [source]
        seen = set([source])
        while queue:
            node = queue.pop(0)
            if node == destination:
                return True
            for n in neighbours[node]:
                if n not in seen:
                    seen.add(n)
                    queue.append(n)
        return False


solution = Solution()
print(solution.validPath(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2))
print(solution.validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5))


