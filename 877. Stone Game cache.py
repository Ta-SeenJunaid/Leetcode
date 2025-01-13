from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(l,r,alice):
            if l>r:
                return 0, 0
            if l==r:
                return 0, piles[l]
            if alice:
                a1, b1 = dp(l+1, r, False)
                a2, b2 = dp(l, r-1, False)
                if a1 +piles[l] > a2 + piles[r]:
                    return a1 +piles[l], b1
                else:
                    return a2 + piles[r], b2
            else:
                a1, b1 = dp(l+1, r, True)
                a2, b2 = dp(l, r-1, True)
                if b1 + piles[l] > b2 + piles[r]:
                    return a1, b1 + piles[l]
                else:
                    return a2, b2 + piles[r]
        a, b = dp(0,len(piles)-1, True)
        return a>b
