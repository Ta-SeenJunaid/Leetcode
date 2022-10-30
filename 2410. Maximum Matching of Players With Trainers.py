from typing import List


# class Solution:
#     def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
#         players.sort()
#         trainers.sort()
#         result = 0
#         trainers_pointer = 0
#         for i in range(len(players)):
#             for j in range(trainers_pointer, len(trainers)):
#                 if players[i] <= trainers[j]:
#                     # print(players[i], trainers[j])
#                     result += 1
#                     trainers_pointer = j+1
#                     break
#         return result

# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/submissions/833553849/
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort()
        result = 0
        for trainer in trainers:
            if players and players[-1] <= trainer:
                result += 1
                players.pop()

        return result


solution = Solution()
print(solution.matchPlayersAndTrainers(players = [4,7,9], trainers = [8,2,5,8]))
print(solution.matchPlayersAndTrainers(players = [1,1,1], trainers = [10]))