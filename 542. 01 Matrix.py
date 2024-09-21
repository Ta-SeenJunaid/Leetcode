class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def is_valid(r, c):
            return 0 <= r < r_len and 0 <= c < c_len
        r_len = len(mat)
        c_len = len(mat[0])
        matrix = [[0 for _ in range(c_len)] for _ in range(r_len)]
        queue = []
        visited = set()
        for r in range(r_len):
            for c in range(c_len):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                r, c, d = queue.pop(0)
                matrix[r][c] = d
                for dr, dc in directions:
                    if (r+dr, c+dc) not in visited and is_valid(r+dr, c+dc):
                        queue.append((r+dr, c+dc, d + 1))
                        visited.add((r+dr, c+dc))
        return matrix
