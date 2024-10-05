class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1] * len(graph)
        stack = []
        for i in range(len(graph)):
            if visited[i] == -1:
                visited[i] = 0
                stack = [i]
                while stack:
                    node = stack.pop()
                    color = visited[node]
                    for nei in graph[node]:
                        if visited[nei] == -1:
                            stack.append(nei)
                            visited[nei] = 1-color
                        elif visited[nei] == color:
                            return False
        return True
