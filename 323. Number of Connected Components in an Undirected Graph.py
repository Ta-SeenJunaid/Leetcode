class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        visited = set()
        stack = []
        cc = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                stack.append(i)
                cc += 1
                while stack:
                    c_node = stack.pop(0)
                    for nei in adj_list[c_node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
        return cc
