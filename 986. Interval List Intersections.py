from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_list_pointer = 0
        second_list_pointer = 0
        answer = []
        first_list_len = len(firstList)
        second_list_len = len(secondList)
        while first_list_pointer < first_list_len and second_list_pointer < second_list_len:
            # two intervals are said to be overlapping if max(start1, start2) <= min(end1, end2)
            max_start = max(firstList[first_list_pointer][0], secondList[second_list_pointer][0])
            min_end = min(firstList[first_list_pointer][1], secondList[second_list_pointer][1])
            if max_start <= min_end:
                answer.append([max_start, min_end])
            # increase the pointer with minimum end time
            if firstList[first_list_pointer][1] < secondList[second_list_pointer][1]:
                first_list_pointer += 1
            else:
                second_list_pointer += 1
        return answer


solution = Solution()
print(solution.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
print(solution.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []))
