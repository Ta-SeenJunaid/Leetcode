import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i[0] for i in collections.Counter(sorted(words)).most_common(k)]


solution = Solution()
print(solution.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
print(solution.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))