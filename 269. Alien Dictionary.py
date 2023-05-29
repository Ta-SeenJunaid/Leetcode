# https://www.youtube.com/watch?v=6kTZYvNNyps
# https://www.youtube.com/watch?v=U3N_je7tWAs&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=26
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words) - 1):
          w1, w2 = words[i], words[i+1]
          min_len = min(len(w1), len(w2))
          if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
          for j in range(min_len):
            if w1[j] != w2[j]:
              adj[w1[j]].add(w2[j])
        # False = visited,  True = current path
        visit = {}
        res = []
        def dfs(c):
          if c in visit:
            return visit[c]
          visit[c] = True
          for nei in adj[c]:
            if dfs(nei):
              return True
          visit[c] = False
          res.append(c)
        for c in adj:
          if dfs(c):
            return ""
        res.reverse()
        return "".join(res)


solution = Solution()
print(solution.alienOrder(words=[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))

solution = Solution()
print(solution.alienOrder(words=[
  "z",
  "x"
]))

solution = Solution()
print(solution.alienOrder(words=[
  "z",
  "x",
  "z"
]))