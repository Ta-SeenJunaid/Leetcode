from typing import List


class Solution:
    def __init__(self):
        self.adj_list = None
        self.result = []
        self.visited = {}

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adj_list = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            self.adj_list[u].append(v)
        for i in range(numCourses):
            if not self.dfs(i):
                return []
        return self.result

    def dfs(self, i):
        if i in self.visited:
            return self.visited[i]
        self.visited[i] = False
        for nei in self.adj_list[i]:
            if not self.dfs(nei):
                return False
        self.visited[i] = True
        self.result.append(i)
        return True


solution = Solution()
print(solution.findOrder(numCourses = 2, prerequisites = [[1,0]]))

solution = Solution()
print(solution.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))

solution = Solution()
print(solution.findOrder(numCourses = 1, prerequisites = []))