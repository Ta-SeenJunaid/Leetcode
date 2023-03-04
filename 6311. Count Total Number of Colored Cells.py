class Solution:
    def coloredCells(self, n: int) -> int:
        return n*n + (n-1)*(n-1)


solution = Solution()
print(solution.coloredCells(n = 1))
print(solution.coloredCells(n = 2))
print(solution.coloredCells(n = 3))
print(solution.coloredCells(n = 4))
print(solution.coloredCells(n = 5))

