# https://www.youtube.com/watch?v=iwv1llyN6mo&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=13
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_dict = {}
        for i in range(len(t)):
            count_dict[t[i]] = count_dict.get(t[i], 0) + 1
        count, l_p = len(count_dict), 0
        ans, min_length = "", float('inf')
        for r_p in range(len(s)):
            if s[r_p] in count_dict:
                count_dict[s[r_p]] -= 1
                if count_dict[s[r_p]] == 0:
                    count -= 1
            while count == 0:
                if r_p-l_p+1 < min_length:
                    min_length = r_p-l_p+1
                    ans = s[l_p:r_p+1]
                if s[l_p] in count_dict:
                    count_dict[s[l_p]] += 1
                    if count_dict[s[l_p]] == 1:
                        count += 1
                l_p += 1
        return ans


solution = Solution()
print(solution.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(solution.minWindow(s = "a", t = "a"))
print(solution.minWindow(s = "a", t = "aa"))