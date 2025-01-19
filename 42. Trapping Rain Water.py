# https://www.youtube.com/watch?v=1_5VuquLbXg
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lp, rp = 0, n-1
        lmax, rmax = 0, 0
        ans = 0
        while lp!=rp:
            if height[lp] <= height[rp]:
                lmax = max(height[lp], lmax)
                if lp != 0:
                    ans += lmax - height[lp]
                lp += 1
            else:
                rmax = max(height[rp], rmax)
                if rp != n-1:
                    ans += rmax - height[rp]
                rp -= 1
        return ans
        
