from collections import defaultdict
from typing import List


# class Solution:
#     def __init__(self):
#         self.adj_list = defaultdict(list)
#         self.visited = set()
#         self.path = set()
#         self.cycle = False
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         for parent, child in prerequisites:
#             self.adj_list[parent].append(child)
#
#         # https://kashifkhan.org/posts/2021-08-13-python-defaultdict-size-changed-error/
#         for i in self.adj_list.copy():
#             if i not in self.visited:
#                 if not self.dfs(i):
#                     return False
#         return True
#
#     def dfs(self, root):
#         self.visited.add(root)
#         self.path.add(root)
#         for child in self.adj_list[root]:
#             if child in self.visited and child in self.path:
#                 self.cycle = True
#                 return False
#             elif child not in self.visited:
#                 self.dfs(child)
#         self.path.remove(root)
#         return False if self.cycle else True

class Solution:
    def __init__(self):
        self.adj_list = None
        self.visited = {}

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj_list = [[] for i in range(numCourses)]
        for u, v in prerequisites:
            self.adj_list[u].append(v)
        for i in range(numCourses):
            if not self.dfs(i, prerequisites):
                return False
        return True
    def dfs(self, root, prerequisites: List[List[int]]):
        if root in self.visited:
            return self.visited[root]
        self.visited[root] = False
        for nei in self.adj_list[root]:
            if not self.dfs(nei, prerequisites):
                return False
        self.visited[root] = True
        return True


solution = Solution()
print(solution.canFinish(numCourses = 2, prerequisites = [[1,0]]))

solution = Solution()
print(solution.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))

solution = Solution()
print(solution.canFinish(numCourses = 6, prerequisites = [[1,0],[2,1], [0,2], [0,3], [4, 5]]))

solution = Solution()
print(solution.canFinish(numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
))