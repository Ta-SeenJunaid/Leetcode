class Solution:
    def reverseVowels(self, s: str) -> str:
        lp, rp = 0, len(s) - 1
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        while lp < rp:
            if s[lp] in vowels and s[rp] in vowels:
                s = s[:lp] + s[rp] + s[lp+1:rp] + s[lp] + s[rp+1:]
                lp += 1
                rp -= 1
            elif s[lp] not in vowels and s[rp] not in vowels:
                lp += 1
                rp -= 1
            elif s[lp] not in vowels:
                lp += 1
            else:
                rp -= 1
        return s
        
