from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_dict = {}
        for i in p:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        count = len(count_dict)
        ans = []
        l_p, r_p = 0, 0
        s_len, p_len = len(s), len(p)
        while r_p < s_len:
            if s[r_p] in count_dict:
                count_dict[s[r_p]] -= 1
                if count_dict[s[r_p]] == 0:
                    count -= 1
            if r_p < p_len-1:
                r_p += 1
            else:
                if count == 0:
                    ans.append(l_p)
                if s[l_p] in count_dict:
                    count_dict[s[l_p]] += 1
                    if count_dict[s[l_p]] == 1:
                        count += 1
                r_p += 1
                l_p += 1
        return ans


solution = Solution()
print(solution.findAnagrams(s = "cbaebabacd", p = "abc"))
print(solution.findAnagrams(s = "abab", p = "ab"))