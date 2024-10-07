class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []:
            return list(range(numCourses))
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        visited = [0]*numCourses # 0: NOT_VISITED, -1: VISITING, 1: VISITED
        is_cycle = False
        topo_ans = []
        def dfs(node):
            nonlocal is_cycle
            if is_cycle:
                return
            if visited[node] == -1:
                is_cycle = True
                return
            if visited[node] == 1:
                return
            visited[node] = -1
            if adj_list[node]:
                for nei in adj_list[node]:
                    dfs(nei)
            topo_ans.append(node)
            visited[node] = 1
            return
        for node in range(numCourses):
            if is_cycle == True:
                return []
            if visited[node] == 0:
                dfs(node)
        return topo_ans[::-1] if not is_cycle else []

        
