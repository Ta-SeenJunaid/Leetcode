from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.queue = []
        self. int_col = None
        self.image = None
        self.r_len = None
        self.c_len = None
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  color: int) -> List[List[int]]:
        self.int_col = image[sr][sc]
        self.image = image
        self.r_len = len(image)
        self.c_len = len(image[0])
        self.dfs_helper(sr, sc, color)
        return self.image


    def dfs_helper(self, sr, sc, color):
        if sr < 0 or sr >= self.r_len or sc < 0 or sc >= self.c_len or (sr, sc) in self.visited or self.image[sr][sc] != self.int_col:
            return
        self.image[sr][sc] = color
        self.visited.add((sr, sc))
        self.dfs_helper(sr+1, sc, color)
        self.dfs_helper(sr-1, sc, color)
        self.dfs_helper(sr, sc+1, color)
        self.dfs_helper(sr, sc-1, color)
        return


solution = Solution()
print(solution.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))

solution = Solution()
print(solution.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))