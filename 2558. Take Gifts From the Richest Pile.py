import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            max_ele = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(math.sqrt(max_ele)))
        return -sum(gifts)

        
