class Solution:
    def __init__(self):
        self.memory = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 0
        if m==1 and n==1:
            return 1

        # As (m,n) & (n,m) belong to same result
        if m > n:
            m, n = n, m
        key = str(m) + ',' + str(n)
        if key in self.memory:
            return self.memory[key]
        self.memory[key] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.memory[key]
