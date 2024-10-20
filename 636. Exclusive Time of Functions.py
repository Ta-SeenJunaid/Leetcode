# https://www.youtube.com/watch?v=CBJI_lZxYU8

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack, prev_start_time = [0]*n, [], 0
        for log in logs:
            id, call, timestamp = log.split(":")
            id, timestamp = int(id), int(timestamp)
            if call == "start":
                if stack:
                    ans[stack[-1]] += timestamp - prev_start_time
                stack.append(id)
                prev_start_time = timestamp
            else:
                ans[stack.pop()] += timestamp - prev_start_time + 1
                prev_start_time = timestamp  + 1
        return ans
        
