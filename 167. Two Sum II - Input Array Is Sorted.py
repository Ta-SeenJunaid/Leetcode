from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            temp = numbers[start]+numbers[end]
            if temp == target:
                return [start+1, end+1]
            elif temp > target:
                end -=1
            else:
                start +=1


solution = Solution()
print(solution.twoSum(numbers = [2,7,11,15], target = 9))
print(solution.twoSum(numbers = [2,3,4], target = 6))
print(solution.twoSum(numbers = [-1,0], target = -1))
