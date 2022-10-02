from string import ascii_letters

# we can use is_alpha method
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l_p = 0
        r_p = len(s)-1
        s_list = list(s)
        while l_p < r_p:
            if s[l_p] not in ascii_letters:
                l_p += 1
            elif s[r_p] not in ascii_letters:
                r_p -= 1
            else:
                s_list[l_p], s_list[r_p] = s_list[r_p], s_list[l_p]
                l_p += 1
                r_p -= 1
        return ''.join(s_list)


solution = Solution()
# print(solution.reverseOnlyLetters(s = "abcdefgh"))
# print(solution.reverseOnlyLetters(s = "abcdefghi"))

print(solution.reverseOnlyLetters(s = "ab-cd"))
print(solution.reverseOnlyLetters(s = "a-bC-dEf-ghIj"))
print(solution.reverseOnlyLetters(s = "Test1ng-Leet=code-Q!"))