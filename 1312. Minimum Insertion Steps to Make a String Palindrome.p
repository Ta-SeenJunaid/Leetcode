class Solution:
    def minInsertions(self, s: str) -> int:
        s_r = s[::-1]
        tb = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for row in range(1, len(s)+1):
            for col in range(1, len(s)+1):
                if s[row-1] == s_r[col-1]:
                    tb[row][col] = 1 + tb[row-1][col-1]
                else:
                    tb[row][col] = max(tb[row-1][col], tb[row][col-1])
        return len(s) - tb[-1][-1]
