from typing import List

class Solution:
    def __init__(self):
        self.result = []
        self.digit_To_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if digits:
            self.backtrack(digits, "")
        return self.result

    def backtrack(self, digits, current_string):
        if not digits:
            self.result.append(current_string)
            return

        for j in self.digit_To_char[digits[0]]:
            self.backtrack(digits[1:], current_string+j)


solution = Solution()
# print(solution.letterCombinations(digits = "234"))
print(solution.letterCombinations(digits = "23"))
# print(solution.letterCombinations(digits = ""))
# print(solution.letterCombinations(digits = "2"))
