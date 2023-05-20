# https://www.youtube.com/watch?v=edXdVwkYHF8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=13
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        len_r = len(mat)
        len_c = len(mat[0])
        visited = set()
        result = [[0 for _ in range(len_c)] for _ in range(len_r)]
        for i in range(len_r):
            for j in range(len_c):
                if mat[i][j] == 0:
                    queue.append([i, j, 0])
                    visited.add((i, j))
        while queue:
            r, c, d = queue.pop(0)
            # if (r, c) not in visited:
            #     visited.add((r,c))
            result[r][c] = d
            if r-1 >= 0 and (r-1, c) not in visited:
                queue.append([r-1, c, d+1])
                visited.add((r-1,c))
            if r+1 < len_r and (r+1, c) not in visited:
                queue.append([r+1, c, d+1])
                visited.add((r+1,c))
            if c-1 >= 0 and (r, c-1) not in visited:
                queue.append([r, c-1, d+1])
                visited.add((r,c-1))
            if c+1 < len_c and (r, c+1) not in visited:
                queue.append([r, c+1, d+1])
                visited.add((r,c+1))
        return result


solution = Solution()
print(solution.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]))
print(solution.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]))
print(solution.updateMatrix(mat = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]))