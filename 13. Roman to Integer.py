class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        symbol_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(len(s)-1):
            if symbol_value[s[i]] >= symbol_value[s[i+1]]:
                result += symbol_value[s[i]]
            else:
                result -= symbol_value[s[i]]

        return result + symbol_value[s[-1]]




solution = Solution()
print(solution.romanToInt(s = "III"))
print(solution.romanToInt(s = "LVIII"))
print(solution.romanToInt(s = "MCMXCIV"))