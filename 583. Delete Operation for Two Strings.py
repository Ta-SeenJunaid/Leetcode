# https://www.youtube.com/watch?v=-fx6aDxcWyg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=31

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        table = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for row in range(1, n+1):
            for col in range(1, m+1):
                if word2[row-1] == word1[col-1]:
                    table[row][col] = 1 + table[row-1][col-1]
                else:
                    table[row][col] = max(table[row-1][col], table[row][col-1])
        return m+n-2*table[-1][-1]

