from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        for i in queries:
            sum_ = count = 0
            for j in nums:
                if j+sum_ <= i:
                    sum_ += j
                    count += 1
                else:
                    continue
            answer.append(count)
        return answer


solution = Solution()
print(solution.answerQueries(nums = [4,5,2,1], queries = [3,10,21]))
print(solution.answerQueries(nums = [2,3,4,5], queries = [1]))