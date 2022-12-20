from typing import List


# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         keys = set([0])
#         for i in rooms[0]:
#             if i not in keys:
#                 keys.add(i)
#         visited = set([0])
#         stack = rooms[0]
#         while stack:
#             current_key = stack.pop()
#             for i in rooms[current_key]:
#                 if i not in keys:
#                     keys.add(i)
#                 if i not in visited:
#                     visited.add(i)
#                     stack.append(i)
#         if len(keys) == len(rooms):
#             return True
#         else:
#             return False


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, stack =  set(), [0]
        while stack:
            node = stack.pop()
            visited.add(node)
            stack.extend([i for i in rooms[node] if i not in visited])
        return len(visited)==len(rooms)


solution = Solution()
print(solution.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
print(solution.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))
print(solution.canVisitAllRooms(rooms = [[2],[],[1]]))
print(solution.canVisitAllRooms(rooms = [[],[2],[1]]))