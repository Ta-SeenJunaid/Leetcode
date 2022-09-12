# https://www.youtube.com/watch?v=iEU2doM224M
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score, left_pointer, right_pointer = 0,0, len(tokens)-1
        while left_pointer <= right_pointer:
            if power >= tokens[left_pointer]:
                power -= tokens[left_pointer]
                score += 1
                left_pointer += 1
            elif score > 0 and left_pointer < right_pointer:
                power += tokens[right_pointer]
                score -= 1
                right_pointer -= 1
            else:
                return score
        return score


solution = Solution()
print(solution.bagOfTokensScore(tokens = [100], power = 50))
print(solution.bagOfTokensScore(tokens = [100,200], power = 150))
print(solution.bagOfTokensScore(tokens = [100,200,300,400], power = 200))

