from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node_num, adj_list = 0, defaultdict(list)
        for i in edges:
            for j in i:
                node_num = max(node_num, j)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        for i in adj_list:
            if len(adj_list[i]) == node_num - 1:
                return i


solution = Solution()
print(solution.findCenter(edges = [[1,2],[2,3],[4,2]]))
print(solution.findCenter(edges = [[1,2],[5,1],[1,3],[1,4]]))