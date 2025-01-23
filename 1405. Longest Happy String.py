import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, [-a, "a"])
        if b > 0:
            heapq.heappush(pq, [-b, "b"])
        if c > 0:
            heapq.heappush(pq, [-c, "c"])
        ans = []
        while pq:
            val, char = heapq.heappop(pq)
            val = -val
            if len(ans) > 1 and ans[-1] == char and ans[-2] == char:
                # tempv, tempc = val, char
                if not pq:
                    break
                cval, cchar = heapq.heappop(pq)
                cval = -cval
                ans.append(cchar)
                cval -= 1
                if cval > 0:
                    heapq.heappush(pq, [-cval, cchar]) 
                heapq.heappush(pq, [-val, char])
            else:
                ans.append(char)
                val -= 1
                if val > 0:
                    heapq.heappush(pq, [-(val), char])
            
        return "".join(ans)
