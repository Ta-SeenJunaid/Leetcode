class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = []
        cc = 0
        t = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                elif grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    cc += 1
        if cc == 0:
            return 0
        if len(queue) == 0:
            return -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                if r+1 < len(grid) and (r+1, c) not in visited and grid[r+1][c] == 1:
                    visited.add((r+1, c))
                    cc -= 1
                    queue.append((r+1, c))
                if r-1 >= 0 and (r-1, c) not in visited and grid[r-1][c] == 1:
                    visited.add((r-1, c))
                    cc -= 1
                    queue.append((r-1, c))
                if c+1 < len(grid[0]) and (r, c+1) not in visited and grid[r][c+1] == 1:
                    visited.add((r, c+1))
                    cc -= 1
                    queue.append((r, c+1))
                if c-1 >= 0 and (r, c-1) not in visited and grid[r][c-1] == 1:
                    visited.add((r, c-1))
                    cc -= 1
                    queue.append((r, c-1))
            t += 1
        if cc != 0:
            return -1
        return t

                
                
