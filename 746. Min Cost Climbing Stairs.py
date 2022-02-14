
# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
#         cost.append(0)
#         cost.append(0)
#         res = [0]*(len(cost))
#
#         for i in range(len(cost)-3, -1, -1):
#
#             res[i]=min(cost[i] + res[i+1], cost[i] + res[i+2])
#
#         return min(res[0],res[1])


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):

            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])


solution = Solution()
print(solution.minCostClimbingStairs([10,15,20]))
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
