# https://www.youtube.com/watch?v=OmYvgK9Rbz0
# https://leetcode.com/problems/di-string-match/discuss/2551549/Simple-bruteforce-solution-for-python-begineer
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        s_len = len(s)
        result = []
        left_pointer, right_pointer = 0, s_len
        for i in s:
            if i == 'I':
                result.append(left_pointer)
                left_pointer += 1
            else:
                result.append(right_pointer)
                right_pointer -= 1
        result.append(left_pointer) if s[-1] == 'D' else result.append(right_pointer)
        return result


solution = Solution()
print(solution.diStringMatch(s = "IDID"))
print(solution.diStringMatch(s = "III"))
print(solution.diStringMatch(s = "DDI"))
