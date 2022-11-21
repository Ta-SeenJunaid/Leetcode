# https://www.youtube.com/watch?v=fCfjOdi6V3g
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        queue = [entrance]
        visited = set()
        visited.add(tuple(entrance))
        result = 0
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                c_row, c_col = queue.pop(0)
                if [c_row, c_col] != entrance and (c_row==0 or c_row==row-1 or c_col==0 or c_col==col-1):
                    return result
                for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    n_row, n_col = c_row+r, c_col+c
                    if 0<=n_row<row and 0<=n_col<col and maze[n_row][n_col]=="." and (n_row,n_col) not in visited:
                        queue.append([n_row,n_col])
                        visited.add((n_row,n_col))
            result += 1
        return -1


solution = Solution()
print(solution.nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
print(solution.nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
print(solution.nearestExit(maze = [[".","+"]], entrance = [0,0]))