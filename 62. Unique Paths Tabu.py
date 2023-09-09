class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tab = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    tab[i][j] = 1
                else: 
                    tab[i][j] = tab[i-1][j] + tab[i][j-1]
        return tab[-1][-1]
        
