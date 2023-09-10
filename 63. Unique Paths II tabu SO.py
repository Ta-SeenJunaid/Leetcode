class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        pre, cur = [0 for _ in range(len(obstacleGrid[0]))], [0 for _ in range(len(obstacleGrid[0]))]
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row==0 and col==0:
                    cur[col] = 1
                elif obstacleGrid[row][col] != 1:
                    cur[col] = (cur[col-1] if col > 0 else 0) + pre[col]
                else:
                    cur[col] = 0
            pre = cur
        return cur[-1]
