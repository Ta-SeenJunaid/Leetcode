class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        left, up, cur = 1, [1 for _ in range(n)], 0
        for i in range(1, m):
            for j in range(1, n):
                cur = left + up[j]
                left, up[j] = cur, cur
            left = 1
        return cur
