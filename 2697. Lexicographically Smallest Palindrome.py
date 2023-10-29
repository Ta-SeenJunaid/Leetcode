class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        lp, rp, s = 0, len(s) - 1, list(s)
        while lp <= rp:
            if s[lp] < s[rp]:
                s[rp] = s[lp]
            elif s[lp] > s[rp]:
                s[lp] = s[rp]
            lp += 1
            rp -= 1
        return "".join(s)
        
