from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in range(0, len(encoded)):
            ans.append(ans[i] ^ encoded[i])
        return ans


solution = Solution()
print(solution.decode(encoded = [1,2,3], first = 1))
print(solution.decode(encoded = [6,2,7,3], first = 4))
