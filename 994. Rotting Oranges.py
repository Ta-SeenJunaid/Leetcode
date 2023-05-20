from typing import List


class Solution:
    def __init__(self):
        self.fresh_orange = 0
        self.queue = []
        self.visited = set()
        self.count = 0
        self.r_len = 0
        self.c_len = 0
        pass
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.r_len = len(grid)
        self.c_len = len(grid[0])
        for i in range(self.r_len):
            for j in range(self.c_len):
                if grid[i][j]==0:
                    continue
                elif grid[i][j] == 2:
                    self.queue.append([i,j])
                else:
                    self.fresh_orange += 1
        if self.fresh_orange == 0:
            return 0
        if len(self.queue) == 0:
            return -1
        while self.queue:
            queue_len = len(self.queue)
            for _ in range(queue_len):
                temp = self.queue.pop(0)
                r, c = temp[0], temp[1]
                # if r < 0 or r >= self.r_len or c < 0 or c >= self.c_len or (r, c) in self.visited or (r, c)!=1:
                #     continue
                if (r, c) not in self.visited:
                    self.visited.add((r,c))
                if r+1 < self.r_len and grid[r+1][c] == 1 and (r+1, c) not in self.visited:
                    # print(r+1, c)
                    self.queue.append([r+1, c])
                    self.fresh_orange -= 1
                    self.visited.add((r+1, c))
                if r-1 >= 0 and grid[r-1][c] == 1 and (r-1, c) not in self.visited:
                    # print(r-1, c)
                    self.queue.append([r-1, c])
                    self.fresh_orange -= 1
                    self.visited.add((r-1, c))
                if c+1 < self.c_len and grid[r][c+1] == 1 and (r, c+1) not in self.visited:
                    # print(r, c+1)
                    self.queue.append([r, c+1])
                    self.fresh_orange -= 1
                    self.visited.add((r, c+1))
                if c-1 >= 0 and grid[r][c-1] == 1 and (r, c-1) not in self.visited:
                    # print(r, c-1)
                    self.queue.append([r, c-1])
                    self.fresh_orange -= 1
                    self.visited.add((r, c-1))
            self.count += 1
        if self.fresh_orange:
            return -1
        return self.count-1



solution = Solution()
print(solution.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))

solution = Solution()
print(solution.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))

solution = Solution()
print(solution.orangesRotting(grid = [[0,2]]))