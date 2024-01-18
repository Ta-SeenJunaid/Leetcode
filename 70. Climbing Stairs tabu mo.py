class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return n
        pre_1 = 1
        pre_2 = 1
        for i in range(2, n+1):
            cur = pre_1 + pre_2
            pre_2 = pre_1
            pre_1 = cur 
        return cur
