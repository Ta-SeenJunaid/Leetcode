# https://www.youtube.com/watch?v=ZjydWQCVg80
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        for p,t in classes:
            heapq.heappush(pq,(-((p+1)/(t+1)-p/t),p,t))
        while extraStudents:
            _, p, t = heapq.heappop(pq)
            p += 1
            t += 1
            heapq.heappush(pq, (-((p+1)/(t+1)-p/t),p,t))
            extraStudents -= 1       
        return sum(p/t for _, p, t in pq)/len(pq)
