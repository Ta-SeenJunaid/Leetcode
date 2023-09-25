class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
