import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [[value,i] for i, value in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            _, i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap, [nums[i], i])
        return nums
        
