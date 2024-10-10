class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if len(grid) == 1:
            return 1
        scp = 0
        queue = [(0,0)]
        while queue:
            scp += 1
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                directions = [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for i, j in directions:
                    nx, ny = x+i, y+j
                    if nx < 0 or nx > n or ny < 0 or ny > n or grid[nx][ny] != 0:
                        continue
                    if nx == n and ny == n:
                        return scp+1
                    grid[nx][ny] = 1
                    queue.append((nx, ny))
        return -1
        
