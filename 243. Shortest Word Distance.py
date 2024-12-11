class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        min_ = n
        p1 = p2 = -1
        for i in range(n):
            if wordsDict[i] == word1:
                p1 = i
            elif wordsDict[i] == word2:
                p2 = i
            if p1!=-1 and p2!=-1:
                min_ = min(min_, abs(p1-p2))
        return min_        
