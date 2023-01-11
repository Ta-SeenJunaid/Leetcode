from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = [pref[0]]
        for i in range(1, len(pref)):
            result.append(pref[i]^pref[i-1])
        return result


solution = Solution()
print(solution.findArray(pref = [5,2,0,3,1]))
print(solution.findArray(pref = [13]))
