class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low, high = 0, len(mat[0]) - 1
        while low <= high:
            mid = (low+high)//2
            row, col = self.find_max(mat, mid)
            if mat[row][col] > (mat[row][col-1] if col > 0 else -1) \
            and mat[row][col] > (mat[row][col+1] if col < (len(mat[0]) - 2) else -1):
                return [row, col]
            elif (mat[row][col-1] if col > 0 else -1) <=  mat[row][col]:
                low = mid + 1
            else:
                high = mid - 1

    def find_max(self, mat: List[List[int]], col_no: int):
        max, row, col = 0, 0, 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] > max:
                    max = mat[r][c]
                    row = r
                    col = c
        return row, col
        
