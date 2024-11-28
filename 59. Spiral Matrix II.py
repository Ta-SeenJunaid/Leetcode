class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(n)]
        right =  True
        left = up = down = False
        count = 1
        i = j = 0
        while (left or right or up or down) and i < n and j < n and matrix[i][j] == -1:
            matrix[i][j] = count
            if left:
                j -=1
                if j < 0 or matrix[i][j] != -1:
                    j += 1
                    i -= 1
                    left = False
                    up = True
            elif right:
                j += 1
                if j >= n or matrix[i][j] != -1:
                    j -= 1
                    i += 1
                    right = False
                    down = True
            elif up:
                i -= 1
                if i < 0 or matrix[i][j] != -1:
                    i += 1
                    j += 1
                    up = False
                    right = True
            elif down:
                i += 1
                if i >= n or matrix[i][j] != -1:
                    i -= 1
                    j -= 1
                    down = False
                    left = True
            count += 1
        return matrix
        
