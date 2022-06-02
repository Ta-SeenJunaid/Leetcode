from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word==word[::-1]:
                return word
        return ""


solution = Solution()
print(solution.firstPalindrome(words = ["abc","car","ada","racecar","cool"]))
print(solution.firstPalindrome(words = ["notapalindrome","racecar"]))
print(solution.firstPalindrome(words = ["def","ghi"]))