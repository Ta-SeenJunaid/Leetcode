from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        visited = set() 
        res = []
        for i, j in prerequisites:
            adj_list[i].append(j)
        def dfs(node, destination):
            visited.add(node)
            if node == destination:
                return True
            for child in adj_list[node]:
                if child not in visited:
                    if dfs(child, destination):
                        return True
            return False
        for u, v in queries:
            res.append(dfs(u,v))
            print(visited)
            visited = set()
        return res
        
