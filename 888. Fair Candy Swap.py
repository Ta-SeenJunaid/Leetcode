# https://leetcode.com/problems/fair-candy-swap/editorial

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        asum, bsum = sum(aliceSizes), sum(bobSizes)
        bset = set(bobSizes)
        for i in aliceSizes:
            if (i + (bsum-asum)/2) in bset:
                return [i, i + (bsum-asum)/2]
