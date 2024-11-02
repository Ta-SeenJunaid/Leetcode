# https://www.youtube.com/watch?v=2g_b1aYTHeg

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(max_heap)
        prev = None
        res = ""
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res
        
