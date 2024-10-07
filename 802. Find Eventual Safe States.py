class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0]*len(graph) # 0: NOT_VISITED, -1: VISITING, 1: VISITED
        topo_res = []
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 1
            return True
        for node in range(len(graph)):
            if dfs(node):
                topo_res.append(node)
        return topo_res
