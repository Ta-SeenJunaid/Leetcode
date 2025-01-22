class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        
        degree.sort()
        value = 1
        ans = 0
        for i in degree:
            ans += i*value
            value += 1
        return ans
        
