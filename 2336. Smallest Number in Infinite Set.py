import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.pq = []       
        for i in range(1,1001):
            self.pq.append(i)
        heapq.heapify(self.pq)

    def popSmallest(self) -> int:
        if self.pq:
            return heapq.heappop(self.pq)

    def addBack(self, num: int) -> None:
        if num not in self.pq:
            heapq.heappush(self.pq, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
