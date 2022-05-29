from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max = 0
        i=1
        for word in words:
            for j in range(i, len(words)):
                if set(word)&set(words[j])==set():
                    temp = len(word)*len(words[j])
                    if temp > max:
                        max = temp
            i +=1
        return max


solution = Solution()
print(solution.maxProduct(words = ["abcw","baz","foo","bar","xtfn","abcdef"]))
print(solution.maxProduct(words = ["a","ab","abc","d","cd","bcd","abcd"]))
print(solution.maxProduct(words = ["a","aa","aaa","aaaa"]))
