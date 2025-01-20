from collections import defaultdict

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = defaultdict(int)
        score_copy = score.copy()
        n = len(score)
        for i in range(n):
            temp[score[i]] = i
        score_copy.sort(reverse=True)
        print(score_copy, temp)
        ans = [""]*n
        for i in range(n):
            if i==0:
                ans[temp[score_copy[i]]] = "Gold Medal"
            elif i ==1:
                ans[temp[score_copy[i]]] = "Silver Medal"
            elif i==2:
                ans[temp[score_copy[i]]] = "Bronze Medal"
            else:
                ans[temp[score_copy[i]]] = str(i+1)      
        return ans
        
