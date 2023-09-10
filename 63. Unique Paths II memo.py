class Solution:
    def __init__(self):
        self.memo = None

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        self.memo = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        return self.dp_re(obstacleGrid, len(obstacleGrid) -1, len(obstacleGrid[0]) -1)

    def dp_re(self, grid: List[List[int]], row: int, col: int) -> int:
        if row == 0 and col == 0:
            return 1
        elif row < 0 or col < 0 or grid[row][col] == 1:
            return 0
        elif self.memo[row][col] != -1:
            return self.memo[row][col]
        else:
            self.memo[row][col] = self.dp_re(grid, row - 1, col) + self.dp_re(grid, row, col - 1)
            return self.memo[row][col]

