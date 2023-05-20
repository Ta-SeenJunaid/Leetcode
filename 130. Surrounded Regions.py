from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.r_len = 0
        self.c_len = 0

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.r_len = len(board)
        self.c_len = len(board[0])
        for j in range(self.c_len):
            if board[0][j] == 'O':
                self.dfs(0, j, board)
            if board[self.r_len-1][j] == 'O':
                self.dfs(self.r_len-1, j, board)
        for i in range(1, self.r_len-1):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][self.c_len-1] == 'O':
                self.dfs(i, self.c_len-1, board)
        for i in range(1, self.r_len-1):
            for j in range(1, self.c_len-1):
                if board[i][j] == 'O' and (i, j) not in self.visited:
                    board[i][j] = 'X'

    def dfs(self, r, c, board: List[List[str]]):
        if r < 0 or r >= self.r_len or c < 0 or c >= self.c_len or (r, c) in self.visited or board[r][c] != 'O':
            return
        self.visited.add((r,c))
        self.dfs(r+1, c, board)
        self.dfs(r-1, c, board)
        self.dfs(r, c+1, board)
        self.dfs(r, c-1, board)
        return


solution = Solution()
print(solution.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))

solution = Solution()
print(solution.solve(board = [["X"]]))

solution = Solution()
print(solution.solve(board = [["O","X","O","O","X","X"],["O","X","X","X","O","X"],["X","O","O","X","O","O"],
                              ["X","O","X","X","X","X"],["O","O","X","O","X","X"],["X","X","O","O","O","O"]]))