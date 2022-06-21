class Solution:
    def sortSentence(self, s: str) -> str:
        dict_w = {}
        for word in s.split():
            dict_w[word[-1]] = word[:-1]
        result = []
        for key in sorted(dict_w):
            result.append(dict_w[key])
        return " ".join(result)


solution = Solution()
print(solution.sortSentence(s = "is2 sentence4 This1 a3"))
print(solution.sortSentence(s = "Myself2 Me1 I4 and3"))