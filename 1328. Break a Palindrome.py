class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s_len = len(palindrome)
        if s_len == 1:
            return ""
        for i in range(s_len):
            if palindrome[i] != 'a':
                temp = palindrome[:i] + 'a' + palindrome[i+1:]
                if temp != temp[::-1]:
                    return temp
        if palindrome[s_len-1] == 'a':
            temp = palindrome[:s_len-1] + 'b'
            if temp != temp[::-1]:
                return temp
        return ""



solution = Solution()
print(solution.breakPalindrome(palindrome = "abccba"))
# print(solution.breakPalindrome(palindrome = "a"))
# print(solution.breakPalindrome(palindrome = "aaaaa"))