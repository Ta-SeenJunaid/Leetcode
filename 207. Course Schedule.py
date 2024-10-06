class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs_helper(i, adj_list, in_path, visited):
            if in_path[i]:
                return True
            if visited[i]:
                return False
            in_path[i] = True
            visited[i] = True
            for nei in adj_list[i]:
                if dfs_helper(nei, adj_list, in_path, visited):
                    return False
            in_path[i] = False
            return False

        adj_list = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            if u == v:
                return False
            adj_list[v].append(u)
        visited = [False]*(numCourses)
        in_path = [False]*(numCourses)

        for i in range(numCourses):
            if dfs_helper(i, adj_list, in_path, visited):
                return False
        return True
        
