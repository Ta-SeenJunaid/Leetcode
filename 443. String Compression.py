from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        l_p, r_p = 0, 0
        answer = []
        for r_p in range(len(chars)):
            if chars[r_p] != chars[l_p]:
                answer.append(chars[l_p])
                if r_p-l_p > 1:
                    for i in list(str(r_p-l_p)):
                        answer.append(i)
                l_p = r_p
        answer.append(chars[l_p])
        if r_p - l_p >= 1:
            for i in list(str(r_p - l_p+1)):
                answer.append(i)
        chars[:] = answer
        # return chars


solution = Solution()
print(solution.compress(chars = ["a","a","b","b","c","c","c"]))
print(solution.compress(chars = ["a"]))
print(solution.compress(chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(solution.compress(chars = ["a","a","a","b","b","a","a"]))

