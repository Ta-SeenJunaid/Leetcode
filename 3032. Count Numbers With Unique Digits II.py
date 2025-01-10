class Solution:
    def numberCount(self, a: int, b: int) -> int:
        ans = 0
        for i in range(a, b+1):
            si = str(i)
            if len(si)== len(set(si)):
                ans += 1
        return ans
