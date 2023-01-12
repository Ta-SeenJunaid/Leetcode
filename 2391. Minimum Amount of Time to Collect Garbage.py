from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        min_time = sum(len(g) for g in garbage)
        g, p, m = 0, 0, 0
        for i in range(len(garbage)-1, 0, -1):
            if g!=0 and p!=0 and m!=0:
                break
            if "G" in garbage[i] and g==0:
                g = sum(travel[:i])
            if "P" in garbage[i] and p==0:
                p = sum(travel[:i])
            if "M" in garbage[i] and m==0:
                m = sum(travel[:i])
        return min_time+g+p+m


solution = Solution()
print(solution.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))
print(solution.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))