# Idea
# https://www.youtube.com/watch?v=4WQouWU9XXE&t=1s
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        rp = len(arr)
        while rp > 0:
            cur_max, cur_max_index = 0, 0
            for idx in range(rp):
                if arr[idx] > cur_max:
                    cur_max_index = idx
                    cur_max = arr[idx]
            res.append(cur_max_index+1)
            arr = arr[:cur_max_index+1][::-1] + arr[cur_max_index+1:]
            res.append(rp)
            arr = arr[:rp][::-1] + arr[rp:]
            rp -= 1
        return res
