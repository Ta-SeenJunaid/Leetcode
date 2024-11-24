class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right = True
        left = down = up = False
        r, c = len(matrix), len(matrix[0])
        i, j = 0 , 0
        ans = []
        while (left or right or down or up) and i < r and j < c and matrix[i][j] != "visited" :
            ans.append(matrix[i][j])
            matrix[i][j] = "visited"
            if left:
                j -= 1
                if j < 0 or (j >= 0 and matrix[i][j] == "visited"):
                    j += 1
                    i -= 1
                    left = False
                    up = True
            elif right:
                j += 1
                if j >= c or ( j < c and matrix[i][j] == "visited"):
                    j -= 1
                    i += 1
                    right = False
                    down = True
            elif down:
                i += 1
                if i >= r or (i < r and matrix[i][j] == "visited"):
                    i -= 1
                    j -= 1
                    down = False
                    left = True
            elif up:
                i -= 1
                if i < 0 or (i >= 0 and matrix[i][j] == "visited"):
                    i += 1
                    j += 1
                    up = False
                    right = True
        return ans
