class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        table = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for row in range(1, m+1):
            for col in range(1, n+1):
                if text2[row-1] == text1[col-1]:
                    table[row][col] = 1 + table[row-1][col-1]
                else:
                    table[row][col] = max(table[row-1][col], table[row][col-1])
        return table[-1][-1]


solution = Solution()
print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
print(solution.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
print(solution.longestCommonSubsequence(text1 = "abc", text2 = "def"))