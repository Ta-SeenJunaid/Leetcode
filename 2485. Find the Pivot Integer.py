class Solution:
    def pivotInteger(self, n: int) -> int:
        p_sum1 = 0
        for i in range(n+1):
            p_sum1 += i
            p_sum2 = 0
            j = i
            while j <=n:
                p_sum2 += j
                j += 1
            if p_sum1 == p_sum2:
                return i
            i += 1
        return -1
