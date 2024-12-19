class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort()
        s.sort()
        gp = 0
        sp = 0
        while gp < len(g) and sp < len(s):
            if g[gp] > s[sp]:
                sp += 1
                continue
            else: 
                ans += 1
            gp += 1
            sp += 1
        return ans
        
