from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        flag_list = [True]*len(groupSizes)

        for i in range(len(groupSizes)):
            count = 0
            temp_list = []
            if flag_list[i]:
                for j in range(i, len(groupSizes)):
                    if groupSizes[i] == groupSizes[j] and flag_list[j]:
                        temp_list.append(j)
                        count += 1
                        flag_list[j] = False
                        if count == groupSizes[i]:
                            result.append(temp_list)
                            break
        return result



solution = Solution()
print(solution.groupThePeople(groupSizes = [3,3,3,3,3,1,3]))
print(solution.groupThePeople(groupSizes = [2,1,3,3,3,2]))
