# https://www.youtube.com/watch?v=h9iTnkgv05E
from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)
        queue = [beginWord]
        visited = set([beginWord])
        result = 1
        while queue:
            for _ in range(len(queue)):
                current_word = queue.pop(0)
                if current_word == endWord:
                    return result
                for j in range(len(current_word)):
                    pattern = current_word[:j] + '*' + current_word[j+1:]
                    for neighbour in nei[pattern]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
            result += 1
        return 0


solution = Solution()
print(solution.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(solution.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))