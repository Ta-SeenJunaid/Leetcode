from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_holder = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= max_holder:
                result.append(True)
            else:
                result.append(False)
        return result


solution =  Solution()
print(solution.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(solution.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(solution.kidsWithCandies(candies = [12,1,12], extraCandies = 10))
