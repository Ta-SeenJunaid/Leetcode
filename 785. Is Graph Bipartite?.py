from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.queue = []
        self.set_a = set()
        self.set_b = set()
    def isBipartite(self, graph: List[List[int]]) -> bool:
        for i in range(len(graph)):
            if i not in self.visited:
                self.bfs(i, i%2, graph)
        return False if self.set_a.intersection(self.set_b) else True

    def bfs(self, root: int, set_g: int, graph: List[List[int]]):
        self.visited.add(root)
        if set_g == 0:
            self.set_a.add(root)
        else:
            self.set_b.add(root)
        self.queue.append(root)
        while self.queue:
            set_g = 1 - set_g
            for _ in range(len(self.queue)):
                current_root = self.queue.pop(0)
                for i in graph[current_root]:
                    if i not in self.visited:
                        self.visited.add(i)
                        self.queue.append(i)
                    if set_g == 0:
                        self.set_a.add(i)
                    else:
                        self.set_b.add(i)
        return



    # def dfs(self, root: int, graph: List[List[int]]):
    #     if root in self.visited:
    #         return
    #     self.visited.add(root)
    #     print(root)
    #     for i in graph[root]:
    #         if i not in self.visited:
    #             self.dfs(i, graph)
    #     return

solution = Solution()
print(solution.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]))

solution = Solution()
print(solution.isBipartite(graph = [[1,3],[0,2],[1,3],[0,2]]))