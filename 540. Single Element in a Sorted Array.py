from collections import Counter
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]


solution =  Solution()
print(solution.singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]));
print(solution.singleNonDuplicate(nums = [3,3,7,7,10,11,11]));

