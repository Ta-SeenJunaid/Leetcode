from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        for c in range(ord(s[0]), ord(s[3])+1):
            for i in range(int(s[1]), int(s[4])+1):
                result.append(chr(c)+str(i))
        return result


solution = Solution()
print(solution.cellsInRange(s = "K1:L2"))
print(solution.cellsInRange(s = "A1:F1"))
