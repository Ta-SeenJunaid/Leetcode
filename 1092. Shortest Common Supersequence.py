# https://www.youtube.com/watch?v=xElxAuBcvsU

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n, scss_string = len(str1), len(str2), ""
        table = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for row in range(1, n+1):
            for col in range(1, m+1):
                if str2[row-1] == str1[col-1]:
                    table[row][col] = 1 + table[row-1][col-1]
                else:
                    table[row][col] = max(table[row-1][col], table[row][col-1])

        row, col = n, m
        while row > 0 and col > 0:
            if str2[row-1] == str1[col-1]:
                scss_string += str2[row-1] 
                row -= 1
                col -= 1
            elif table[row-1][col] > table[row][col-1]:
                scss_string += str2[row-1]
                row -= 1
            else:
                scss_string += str1[col-1]
                col -= 1
        while row > 0:
            scss_string += str2[row-1]
            row -= 1
        while col > 0:
            scss_string += str1[col-1]
            col -= 1
        return scss_string[::-1]
