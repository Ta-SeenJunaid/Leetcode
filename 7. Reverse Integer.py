class Solution:
    def reverse(self, x: int) -> int:
        minv = -2**31
        maxv = 2**31-1
        if x >= 0:
            val = int(str(x)[::-1]) 
        else:
            val = -int(str(abs(x))[::-1])
        if val < minv or val > maxv:
            return 0
        return val
        
        
