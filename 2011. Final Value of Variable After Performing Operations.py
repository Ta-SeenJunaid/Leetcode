from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for operation in operations:
            if operation == "X++" or operation == "++X":
                ans += 1
            else:
                ans -=1
        return ans


solution = Solution()
print(solution.finalValueAfterOperations(operations = ["--X","X++","X++"]))
print(solution.finalValueAfterOperations(operations = ["++X","++X","X++"]))
print(solution.finalValueAfterOperations(operations = ["X++","++X","--X","X--"]))