# https://www.youtube.com/watch?v=RR1n-d4oYqE
import heapq
from typing import List


# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         tasks_len = len(tasks)
#         for i in range(len(tasks)):
#             tasks[i].append(i)
#         tasks.sort()
#
#         heap, current_time= [[tasks[0][1], tasks[0][2]]], tasks[0][0]
#         pointer, ans,  remaining_processing_time = 1, [], 0
#         while True:
#             for i in range(pointer, tasks_len):
#                 if tasks[pointer][0] == current_time:
#                     heapq.heappush(heap, [tasks[pointer][1], tasks[pointer][2]])
#                     pointer += 1
#                 else:
#                     break
#             if remaining_processing_time == 0:
#                 processing_time, index = heapq.heappop(heap)
#                 remaining_processing_time = processing_time
#                 ans.append(index)
#                 if len(ans) == len(tasks):
#                     break
#             current_time += 1
#             if remaining_processing_time > 0:
#                 remaining_processing_time -= 1
#         return ans

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_len = len(tasks)
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        heap, current_time= [], tasks[0][0]
        pointer, ans,  remaining_processing_time = 0, [], 0
        while heap or pointer < tasks_len:
            while pointer < tasks_len and current_time >= tasks[pointer][0]:
                heapq.heappush(heap, [tasks[pointer][1], tasks[pointer][2]])
                pointer += 1
            if not heap:
                current_time = tasks[pointer][0]
            else:
                processing_time, index = heapq.heappop(heap)
                current_time += processing_time
                ans.append(index)
        return ans


solution = Solution()
print(solution.getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]))
print(solution.getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]))
print(solution.getOrder(tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))




