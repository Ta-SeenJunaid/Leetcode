# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return self.fib(n-1) + self.fib(n-2)

# Dynamic programming
class Solution(object):
    def __init__(self):
        self.memory = {}
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.memory:
            return self.memory[n]
        self.memory[n] = self.fib(n-1) + self.fib(n-2)
        return self.memory[n]


solution = Solution()
print(solution.fib(30))
print(solution.fib(40))