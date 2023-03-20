class Solution:
    def __init__(self):
        self.memo = 0

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = [[-1 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in range(len(text1)+1):
            self.memo[0][i] = 0
        for j in range(len(text2)+1):
            self.memo[j][0] = 0
        return self.lcs(text1, text2)

    def lcs(self, text1, text2):
        if len(text1) == 0 or len(text2) == 0:
            return 0
        elif self.memo[len(text2)][len(text1)] != -1:
            return self.memo[len(text2)][len(text1)]
        elif text1[-1] == text2[-1]:
            self.memo[len(text2)][len(text1)] =  1 + self.lcs(text1[:-1], text2[:-1])
            return self.memo[len(text2)][len(text1)]
        else:
            self.memo[len(text2)][len(text1)] = max(self.lcs(text1[:-1], text2),
                                                    self.lcs(text1, text2[:-1]))
            return self.memo[len(text2)][len(text1)]


solution = Solution()
print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
print(solution.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
print(solution.longestCommonSubsequence(text1 = "abc", text2 = "def"))