class Solution:
    def __init__(self):
        self.memo = None
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp_re(m-1, n-1)

    def dp_re(self, m:int, n:int) -> int:
        if m==0 and n==0:
            return 1
        if m < 0 or n < 0:
            return 0
        if self.memo[m][n] != -1:
            return self.memo[m][n]
        self.memo[m][n] = self.dp_re(m-1,n) + self.dp_re(m, n-1)
        return self.memo[m][n]
        
