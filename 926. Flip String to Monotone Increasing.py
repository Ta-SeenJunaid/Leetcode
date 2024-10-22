# https://www.youtube.com/watch?v=k7pwIcvMqDY

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num_1 = 0
        for c in s:
            if c=="0":
                ans = min(num_1, ans+1)
            else:
                num_1 += 1
        return ans
        
