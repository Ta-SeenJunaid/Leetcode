class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')


solution = Solution()
print(solution.interpret(command = "G()(al)"))
print(solution.interpret(command = "G()()()()(al)"))
print(solution.interpret(command = "(al)G(al)()()G"))
