class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiopQWERTYUIOP"
        r2 = "asdfghjklASDFGHJKL"
        r3 = "zxcvbnmZXCVBNM"
        ans = []
        for word in words:
            if word[0] in r1:
                temp = r1
            elif word[0] in r2:
                temp = r2
            else:
                temp = r3
            for cha in word:
                if cha not in temp:
                    temp = None
                    break
            if temp:
                ans.append(word)
        return ans
