class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur_pil_pos = 1
        direction = 1
        cur_time = 1
        while cur_time <= time:
            if 1 <= cur_pil_pos + direction <= n:
                cur_pil_pos += direction
                cur_time += 1
            else:
                direction *= -1
        return cur_pil_pos
        
