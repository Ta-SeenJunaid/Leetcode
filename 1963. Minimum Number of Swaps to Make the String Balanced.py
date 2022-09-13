class Solution:
    def minSwaps(self, s: str) -> int:
        s_len = len(s)
        swap = 0
        opening_brackets, closing_brackets = 0, 0
        left_pointer, right_pointer = 0, len(s)-1
        while left_pointer < right_pointer:
            if s[left_pointer] == "[":
                opening_brackets += 1
            elif s[left_pointer] == "]":
                closing_brackets += 1
            if closing_brackets > opening_brackets:
                for i in range(right_pointer, left_pointer, -1):
                    right_pointer -= 1
                    if s[i] == "[":
                        swap += 1
                        closing_brackets -= 1
                        opening_brackets += 1
                        break
            left_pointer += 1
        return swap


solution = Solution()
print(solution.minSwaps(s = "][]["))
print(solution.minSwaps(s = "]]][[["))
print(solution.minSwaps(s = "[]"))

