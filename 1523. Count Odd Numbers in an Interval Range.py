# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/solutions/3178185/0ms-beats-100-full-explanation-1-line-formula-c-java-python3/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - low//2


solution = Solution()
print(solution.countOdds(low = 3, high = 7))
print(solution.countOdds(low = 8, high = 10))
