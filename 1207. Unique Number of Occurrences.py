from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        fre_dict = {}
        for i in arr:
            if i in fre_dict:
                fre_dict[i] += 1
            else:
                fre_dict[i] = 1
        unique_fre = set()
        for i in fre_dict:
            if fre_dict[i] in unique_fre:
                return False
            else:
                unique_fre.add(fre_dict[i])
        return True


solution = Solution()
print(solution.uniqueOccurrences(arr = [1,2,2,1,1,3]))
print(solution.uniqueOccurrences(arr = [1,2]))
print(solution.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))