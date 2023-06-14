# https://www.youtube.com/watch?v=0ytpZyiZFhA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=40
from typing import List
from heapq import heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        len_r, len_c = len(heights), len(heights[0])
        temp = [[float('inf') for _ in range(len_c)] for _ in range(len_r)]
        temp[0][0] = 0
        min_heap = [(0, 0, 0)]
        d_r = [1, 0, -1, 0]
        d_c = [0, 1, 0, -1]
        while min_heap:
            # print(min_heap)
            w, r, c = heappop(min_heap)
            if r==len_r-1 and c==len_c-1:
                return w
            for i in range(4):
                n_r = r + d_r[i]
                n_c = c + d_c[i]
                if 0 <= n_r < len_r and 0 <= n_c < len_c and max(abs(heights[n_r][n_c] - heights[r][c]), w) < temp[n_r][n_c]:
                    temp[n_r][n_c] = max(abs(heights[n_r][n_c] - heights[r][c]), w)
                    heappush(min_heap, (temp[n_r][n_c], n_r, n_c))


solution = Solution()
print(solution.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))

solution = Solution()
print(solution.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]))

solution = Solution()
print(solution.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],
                                            [1,2,1,2,1],[1,1,1,2,1]]))

solution = Solution()
print(solution.minimumEffortPath(heights = [[1,10,6,7,9,10,4,9]]))