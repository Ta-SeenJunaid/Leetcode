class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        def dfs_helper(r, c, board):
            if r < 0 or c < 0 or r == len(board) or c == len(board[0]):
                return
            elif board[r][c] == "X":
                return
            elif (r, c) not in visited:
                visited.add((r,c))
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for rd, cd in directions:
                    dfs_helper(r+rd, c+cd, board)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or row == len(board)-1 or col == 0 or col ==len(board[0])-1 ) and board[row][col] == "O":
                    dfs_helper(row, col, board) 

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited:
                    print(row, col)
                    board[row][col] = "X"               

