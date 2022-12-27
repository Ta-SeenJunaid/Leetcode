from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        result = 0
        temp = []
        for i in range(len(capacity)):
            temp.append([capacity[i]-rocks[i], i])
        temp.sort()
        for space, index in temp:
            current_space = space
            if current_space > 0 and additionalRocks > 0:
                if current_space < additionalRocks:
                    additionalRocks -= current_space
                    rocks[index] += current_space
                else:
                    rocks[index] += additionalRocks
                    additionalRocks = 0
            if capacity[index] == rocks[index]:
                result += 1
        return result

solution = Solution()
print(solution.maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2))
print(solution.maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100))
print(solution.maximumBags(capacity = [91,54,63,99,24,45,78]
, rocks = [35,32,45,98,6,1,25], additionalRocks = 17))