from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = ''
        for i in range(0, len(digits)):
            sum = sum + str(digits[i])

        return list(map(int, list(str(int(sum) + 1))))


solution = Solution()
print(solution.plusOne(digits = [1,2,3]))
print(solution.plusOne(digits = [4,3,2,1]))
print(solution.plusOne(digits = [9]))
