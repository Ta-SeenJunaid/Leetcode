class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        visited = [0] * numCourses  # 0: NOT_VISITED, -1: VISITING, 1: VISITED
        
        def dfs(node):
            if visited[node] == -1:  # Cycle detected (currently in the same path)
                return False
            if visited[node] == 1:   # Node has already been processed
                return True
            
            visited[node] = -1  # Mark node as "VISITING"
            
            for neighbor in adj_list[node]:
                if not dfs(neighbor):  # If any neighbor leads to a cycle
                    return False
            
            visited[node] = 1  # Mark node as fully processed ("VISITED")
            return True
        
        # Start DFS from each course (in case of disconnected components)
        for node in range(numCourses):
            if visited[node] == 0:  # Start DFS only for unvisited nodes
                if not dfs(node):   # If a cycle is detected, return False
                    return False
        
        return True  # If no cycle is detected, all courses can be finished
