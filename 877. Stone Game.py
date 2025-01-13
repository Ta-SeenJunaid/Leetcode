class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(l,r,alice):
            if l>r:
                return 0, 0
            elif l==r:
                return 0, piles[l]
            elif (l, r, alice) in memo:
                return memo[(l, r, alice)]
            if alice:
                a1, b1 = dp(l+1, r, False)
                a2, b2 = dp(l, r-1, False)
                a1 = a1 + piles[l]
                a2 = a2 + piles[r]
                if a1 > a2:
                    memo[(l, r, alice)] = a1, b1
                    return a1, b1
                else:
                    memo[(l, r, alice)] = a2, b2
                    return a2, b2
            else:
                a1, b1 = dp(l+1, r, True) 
                a2, b2 = dp(l, r-1, True)
                b1 = b1 + piles[l]
                b2 = b2 + piles[r]
                if b1 > b2:
                    memo[(l, r, alice)] = a1, b1
                    return a1, b1
                else:
                    memo[(l, r, alice)] = a2, b2
                    return a2, b2
        a, b = dp(0,len(piles)-1, True)
        return a>b
