# https://leetcode.com/problems/spiral-matrix-iii/editorial/
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [[0,1],[1,0], [0, -1], [-1, 0]]
        tra = []
        steps = 1
        cur_dir = 0
        while len(tra) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                        tra.append([rStart, cStart])
                    rStart += dir[cur_dir][0]
                    cStart += dir[cur_dir][1]
                cur_dir = (cur_dir+1) % 4
            steps += 1
        return tra
        
