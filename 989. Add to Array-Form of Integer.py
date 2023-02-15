from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(i) for i in str((int(''.join(str(c)  for c in num)) + k))]


solution = Solution()
print(solution.addToArrayForm(num = [1,2,0,0], k = 34))
print(solution.addToArrayForm(num = [2,7,4], k = 181))
print(solution.addToArrayForm(num = [2,1,5], k = 806))