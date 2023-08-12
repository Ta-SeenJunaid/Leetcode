# https://www.youtube.com/watch?v=wuOOOATz_IA&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=27

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_r = s[::-1]
        tb = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for row in range(1, len(s)+1):
            for col in range(1, len(s)+1):
                if s[col-1] == s_r[row-1]:
                    tb[row][col] = 1 + tb[row-1][col-1]
                else:
                    tb[row][col] = max(tb[row-1][col], tb[row][col-1])
        return tb[-1][-1]
