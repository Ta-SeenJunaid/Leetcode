# https://www.youtube.com/watch?v=5e_kVxHrrtE
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        output = []
        for row, vector in enumerate(mat):
            count_soldiers = [sum(vector), row]
            output.append(count_soldiers)

        output.sort()
        return [i[1] for i in output[:k]]


solution = Solution()
print(solution.kWeakestRows(mat=
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))
print(solution.kWeakestRows(mat=
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))
