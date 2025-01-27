class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for edge in edges:
            in_degree[edge[1]] += 1
        ans = -1
        c_o = 0
        for i in range(n):
            if in_degree[i] == 0:
                c_o += 1
                ans = i
            if c_o > 1:
                return -1 
        return ans
        
