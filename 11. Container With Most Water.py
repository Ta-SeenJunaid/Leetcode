class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        mw = 0
        while lp < rp:
            mw = max(mw, min(height[lp], height[rp])*(rp-lp))
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return mw
        
