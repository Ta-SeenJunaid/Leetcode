from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for account in accounts:
            max_sum = max(max_sum, sum(account))
        return max_sum


solution = Solution()
print(solution.maximumWealth(accounts = [[1,2,3],[3,2,1]]))
print(solution.maximumWealth(accounts = [[1,5],[7,3],[3,5]]))
print(solution.maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))
