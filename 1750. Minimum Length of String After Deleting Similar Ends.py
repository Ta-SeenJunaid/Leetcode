class Solution:
    def minimumLength(self, s: str) -> int:
        lp, rp = 0, len(s)-1
        while lp < rp and s[lp] == s[rp]:
            temp = s[lp]
            while lp <= rp and s[lp] == temp:
                lp += 1
            while rp > lp and s[rp] == temp:
                rp -=  1
        return rp - lp + 1
        
