# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/solutions/2995109/python-3-1-6-lines-w-example-t-m-97-32/
from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        if len(tasks) == 1:
            return -1
        tasks = Counter(tasks)
        if 1 in tasks.values():
            return -1
        result = 0
        for n in tasks.values():
            result += n//3 + bool(n%3)
        return result


solution = Solution()
print(solution.minimumRounds(tasks = [2,2,3,3,2,4,4,4,4,4]))
print(solution.minimumRounds(tasks = [2,3,3]))
print(solution.minimumRounds(tasks = [5,5,5,5]))