# https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand

class Solution:
    def __init__(self):
        self.ans = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs(0, 0, '', n)
        return self.ans

    def dfs(self, left, right, s, n):
        if len(s) == 2 * n:
            self.ans.append(s)
            return
        if left < n:
            self.dfs(left + 1, right, s + '(', n)
        if right < left:
            self.dfs(left, right+1, s + ')', n)
