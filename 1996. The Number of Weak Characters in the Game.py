# https://www.youtube.com/watch?v=s21et-TSkkk
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key= lambda x:(-x[0], x[1]))
        max_defense = 0
        weak_characters = 0
        for i in properties:
            if i[1] < max_defense:
                weak_characters += 1
            max_defense = max(max_defense, i[1])
        return weak_characters




solution = Solution()
print(solution.numberOfWeakCharacters(properties = [[5,5],[6,3],[3,6]]))
print(solution.numberOfWeakCharacters(properties = [[2,2],[3,3]]))
print(solution.numberOfWeakCharacters(properties = [[1,5],[10,4],[4,3]]))
print(solution.numberOfWeakCharacters(properties = [[1,1],[2,1],[2,2],[1,2]]))
