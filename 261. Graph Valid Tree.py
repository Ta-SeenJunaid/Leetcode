class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj_list = [[] for _ in range(n)]
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                if nei in seen:
                    continue
                seen.add(nei)
                stack.append(nei)
        return len(seen) == n
