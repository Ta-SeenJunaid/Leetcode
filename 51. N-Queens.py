class Solution:
    def __init__(self):
        self.ans = []
        self.graph = None
        self.col = set()
        self.pos_diag = set()
        self.neg_diag = set()

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.graph = [["." for _ in range(n)] for _ in range(n)]
        self.backtrack(0, n)
        return self.ans

    def backtrack(self, r, n):
        if r == n:
            cur_graph = ["".join(row) for row in self.graph]
            self.ans.append(cur_graph)
            return

        for c in range(n):
            if c in self.col or (r+c) in self.pos_diag or (r-c) in self.neg_diag:
                continue
            self.col.add(c)
            self.pos_diag.add(r+c)
            self.neg_diag.add(r-c)
            self.graph[r][c] = "Q"

            self.backtrack(r+1, n)

            self.col.remove(c)
            self.pos_diag.remove(r+c)
            self.neg_diag.remove(r-c)
            self.graph[r][c] = "."
             
        
