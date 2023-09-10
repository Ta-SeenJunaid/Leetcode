class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        tab = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row==0 and col==0:
                    tab[row][col] = 1
                elif obstacleGrid[row][col] != 1:
                    tab[row][col] = (tab[row - 1][col] if row > 0 else 0) \
                    + (tab[row][col - 1] if col > 0 else 0)
                else:
                    tab[row][col] = 0 
        return tab[-1][-1]
