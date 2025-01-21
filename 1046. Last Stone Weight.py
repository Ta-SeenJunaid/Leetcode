import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i in stones:
            heapq.heappush(pq, -i)
        while len(pq) >=2:
            x = -heapq.heappop(pq)
            y= -heapq.heappop(pq)
            if x!=y:
                heapq.heappush(pq, -(x-y))
        return -pq[0] if pq else 0
        
