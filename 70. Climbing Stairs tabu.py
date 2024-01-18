class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        tab = [0 for _ in range(n+1)]
        tab[0] = 1
        tab[1] = 1
        for i in range(2, n+1):
            tab[i] = tab[i-1] + tab[i-2]
        return tab[-1]
