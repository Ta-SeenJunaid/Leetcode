import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        heapq.heapify(sticks)
        while len(sticks) >= 2:
            min1 = heapq.heappop(sticks)
            min2 = heapq.heappop(sticks)
            cost = min1+min2
            ans += cost
            heapq.heappush(sticks, cost)
        return ans
