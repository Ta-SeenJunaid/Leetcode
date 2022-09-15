# https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100
# https://www.youtube.com/watch?v=PV2p54ZXvLI
import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        frequency = collections.Counter(changed)
        if frequency[0] % 2:
            return []
        for i in sorted(frequency):
            if frequency[i] > frequency[2*i]:
                return []
            frequency[2*i] -= frequency[i] if i else frequency[i]//2

        return list(frequency.elements())


solution = Solution()
print(solution.findOriginalArray(changed = [1,3,4,2,6,8]))
print(solution.findOriginalArray(changed = [6,3,0,1]))
print(solution.findOriginalArray(changed = [1]))
print(solution.findOriginalArray(changed = [0,0,0,0]))
print(solution.findOriginalArray(changed = [2,1,2,4,2,4]))