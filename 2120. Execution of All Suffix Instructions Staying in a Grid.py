from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range(0, len(s)):
            current_position = [startPos[0], startPos[1]]
            count = 0
            for j in range(i, len(s)):
                if s[j] == 'R':
                    current_position[1] = current_position[1] + 1
                    if current_position[1] > n-1:
                        break
                    count += 1
                elif s[j] == 'L':
                    current_position[1] = current_position[1] - 1
                    if current_position[1] < 0:
                        break
                    count += 1
                elif s[j] == 'D':
                    current_position[0] = current_position[0] + 1
                    if current_position[0] > n-1:
                        break
                    count += 1
                else:
                    current_position[0] = current_position[0] - 1
                    if current_position[0] < 0:
                        break
                    count += 1

            result.append(count)
        return result


solution = Solution()
print(solution.executeInstructions(n = 3, startPos = [0,1], s = "RRDDLU"))
print(solution.executeInstructions(n = 2, startPos = [1,1], s = "LURD"))
print(solution.executeInstructions(n = 1, startPos = [0,0], s = "LRUD"))