from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None]*len(indices)
        for i in range(len(indices)):
            ans[indices[i]] = s[i]
        return ''.join(ans)


solution = Solution()
print(solution.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(solution.restoreString(s = "abc", indices = [0,1,2]))
